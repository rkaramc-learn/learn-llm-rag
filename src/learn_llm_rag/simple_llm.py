import logging

from langchain_ollama import OllamaLLM
from .learn_utils import Timer

logger = logging.getLogger(__name__)


def SimpleLLM():
    # Initialize LLM with remote URL and available model
    logger.info("Configuring the Ollama LLM...")
    model = OllamaLLM(
        base_url="http://quark02.saury-gar.ts.net:11434",
        model="llama3.2:latest",
        format="json",
    )

    def query(question, *, llm=model):
        logger.info(f"Query to the LLM: {question}")
        with Timer("Invoking LLM with question...", _logger=logger):
            response = llm.invoke(question)
        logger.info(f"Received response: {response.strip()}")
        return response

    return query
