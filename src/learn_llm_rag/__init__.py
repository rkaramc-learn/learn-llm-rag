import logging
import os

from dotenv import load_dotenv

from learn_llm_rag.learn_utils import Timer
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


def print_response(response):
    prev_chunk = ""
    # printable = ""
    for chunk in response:
        # print(f"A->(`{chunk}`, `{prev_chunk}`, `{printable}`)")
        if chunk.strip() == "":
            prev_chunk += chunk
            # print(f"B->(`{chunk}`, `{prev_chunk}`, `{printable}`)")
            continue
        if prev_chunk.strip() == "":
            prev_chunk += chunk
            # print(f"C->(`{chunk}`, `{prev_chunk}`, `{printable}`)")
        # printable += prev_chunk
        print(prev_chunk, end="", flush=True)
        prev_chunk = ""
        # print(f"D->(`{chunk}`, `{prev_chunk}`, `{printable}`)")
    # print("{", end="", flush=True)
    # print(printable, end="", flush=True)
    print()


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

        Question: {question}

        Response: Let's think step by step.
        """
        stream_mode_flag = os.getenv("LLM_STREAM_MODE", False)

        # Print response
        for i in range(3):
            logger.info(f"Printing the response... (Iteration {i+1})")
            if stream_mode_flag:
                with Timer("Streaming LLM with question..."):
                    llm_response = llm.query_with_stream(
                        question, prompt_template=template
                    )
                    print("A: ", end="", flush=True)
                    print_response(llm_response)
                    # print("A: ", end="", flush=True)
                    # for chunk in llm_response:
                    #     print(chunk, end="", flush=True)
                    # print()
            else:
                llm_response = llm.query(question, prompt_template=template)
                print_response(llm_response)
                # print(f"A: {llm_response.strip()}")

    except Exception as e:
        logger.exception(
            f"{type(e).__name__} occurred when generating response.", exc_info=e
        )
        return


def main():
    logger.info("=" * 80)
    logger.info("Starting Simple LLM Caller...")
    callSimpleLLM()
    logger.info("End of Simple LLM Caller")


if __name__ == "__main__":
    main()
