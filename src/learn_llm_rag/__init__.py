import logging

from dotenv import load_dotenv  # [Step 1.4c]

from learn_llm_rag.simple_llm import SimpleLLM

streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("learn_llm_rag.log"), streamHandler],
)
logger = logging.getLogger(__name__)


load_dotenv()  # [Step 1.4c]


def callSimpleLLM():
    try:
        # Setup question
        question = (
            "What are the population projections for India for the next 50 years?"
        )
        print(f"Q: {question}")

        # Initialize LLM with remote URL and available model
        logger.info("Initializing the LLM wrapper...")
        llm_query = SimpleLLM()

        # Query LLM
        logger.info("Querying the LLM...")
        llm_response = llm_query(question)

        # Print response
        logger.info("Printing the response...")
        print(f"A: {llm_response.strip()}")

    except Exception as e:
        # [Step 1.4a] begins
        logger.error(f"{type(e).__name__}: {e.__notes__}{e}")
        return
        # [Step 1.4a] ends


def main():
    logger.info("=" * 80)
    logger.info("Starting Simple LLM Caller...")
    callSimpleLLM()
    logger.info("End of Simple LLM Caller")


if __name__ == "__main__":
    main()
