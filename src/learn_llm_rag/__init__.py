import logging
import os

from dotenv import load_dotenv

from learn_llm_rag.simple_llm import SimpleLLM

streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("learn_llm_rag.log"), streamHandler],
)
logger = logging.getLogger(__name__)


load_dotenv()


def callSimpleLLM():
    try:
        # Setup question
        question = (
            "What are the population projections for India for the next 50 years?"
        )
        print(f"Q: {question}")

        # Initialize LLM with remote URL and available model
        logger.info("Initializing the LLM wrapper...")
        llm = SimpleLLM()

        # Query LLM
        logger.info("Querying the LLM...")

        template = """
        You are a helpful, respectful, and honest assistant.
        Follow a chain-of-thoughts format when generating the response.
        Based on the chain of thoughts, the final answer should be listed at the end of the response.

        Question: {question}

        Response: Let's think step by step.
        """
        stream_mode_flag = os.getenv("LLM_STREAM_MODE", False)

        # Print response
        logger.info("Printing the response...")
        if stream_mode_flag:
            llm_response = llm.query_with_stream(question, prompt_template=template)
            print("A: ", end="", flush=True)
            for chunk in llm_response:
                if stream_mode_flag and chunk.strip() == "":
                    continue
                print(chunk, end="", flush=True)
            print()
        else:
            llm_response = llm.query(question, prompt_template=template)
            print(f"A: {llm_response.strip()}")

    except Exception as e:
        logger.error(f"{type(e).__name__}: {e.__notes__}{e}")
        return


def main():
    logger.info("=" * 80)
    logger.info("Starting Simple LLM Caller...")
    callSimpleLLM()
    logger.info("End of Simple LLM Caller")


if __name__ == "__main__":
    main()
