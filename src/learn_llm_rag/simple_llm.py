import logging
import os

import httpx
from langchain_ollama import OllamaLLM

from learn_llm_rag.learn_utils import Timer

logger = logging.getLogger(__name__)


class OllamaLLMServer:
    def __init__(self, *, base_url: str, model: str) -> None:
        """
        Initialize Ollama LLM wrapper with remote URL and model name.
        """
        (self._base_url, self._model) = self._validate_ollama_url_and_model(
            base_url, model
        )

        self.llm = OllamaLLM(base_url=self._base_url, model=self._model, format="json")

    def query(self, question, *, prompt_template="{question}"):
        logger.info(f"Query to the LLM: {question}")
        with Timer("Invoking LLM with question...", _logger=logger):
            prompt = prompt_template.format(question=question)
            response = self.llm.invoke(prompt)
            response = response.strip()
        logger.info(f"Received response: {response}")
        return response

    def _validate_ollama_url_and_model(self, base_url, model):
        try:
            response = httpx.get(
                f"{base_url}/api/tags"  # Ollama API to get list of models
            )
            response.raise_for_status()
            tags = response.json()
            models = next(
                (
                    model_dict
                    for model_dict in tags["models"]
                    if model_dict["name"] == model
                ),
                None,
            )
            if models is None:
                raise ValueError(f"Model <{model}> not found at {base_url}")
            return (base_url, model)
        except (httpx.ConnectError, httpx.ConnectTimeout) as e:
            e.add_note(f"Error connecting to Ollama {base_url} for {model}")
            raise e from None


def SimpleLLM():
    """
    Return an instance of OllamaLLMServer with the remote URL and model
    configured from environment variables.
    """
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "llama3.2:latest")

    return OllamaLLMServer(base_url=base_url, model=model)
