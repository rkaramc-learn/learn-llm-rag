from learn_llm_rag.simple_llm import SimpleLLM


def callSimpleLLM():
    # Setup question
    question = "What are the population projections for India for the next 50 years?"
    print(f"Q: {question}")

    # Initialize LLM with remote URL and available model
    llm_query = SimpleLLM()

    # Query LLM
    llm_response = llm_query(question)
    print(f"A: {llm_response.strip()}")


def main():
    callSimpleLLM()


if __name__ == "__main__":
    main()
