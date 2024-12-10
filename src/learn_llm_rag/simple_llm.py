import logging
import os

import httpx
from langchain_ollama import OllamaLLM

from learn_llm_rag.learn_utils import Timer

logger = logging.getLogger(__name__)


def SimpleLLM():
    # Initialize LLM with remote URL and available model
    logger.info("Configuring the Ollama LLM...")

    # [Step 1.4b] begins
    def _validate_ollama_url_and_model(base_url, model):
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
        except httpx.ConnectError as e:
            e.add_note(f"Error connecting to Ollama {base_url} for {model}")
            raise e from None

    (_base_url, _model) = _validate_ollama_url_and_model(
        # [Step 1.4c] begins
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        model=os.getenv("OLLAMA_MODEL", "llama3.2:latest"),
        # [Step 1.4c] ends
    )
    # [Step 1.4b] ends

    model = OllamaLLM(
        base_url=_base_url,
        model=_model,
        format="json",
    )

    def query(question, *, llm=model, prompt_template="{question}"):
        logger.info(f"Query to the LLM: {question}")
        with Timer("Invoking LLM with question...", _logger=logger):
            # [Step 1.4d] begins
            prompt = prompt_template.format(question=question)
            # [Step 1.4d] ends
            response = llm.invoke(prompt)
        logger.info(f"Received response: {response.strip()}")
        return response

    return query
