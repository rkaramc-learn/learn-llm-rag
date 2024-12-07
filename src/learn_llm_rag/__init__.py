from langchain_ollama import OllamaLLM


def callSimpleLLM():
    # Setup question
    question = "What are the population projections for India for the next 50 years?"
    print(f"Q: {question}")

    # Initialize LLM with remote URL and available model
    llm = OllamaLLM(
        base_url="http://quark02.saury-gar.ts.net:11434",
        model="llama3.2:latest",
        format="json",
    )

    # Query LLM
    llm_response = llm.invoke(question)
    print(f"A: {llm_response.strip()}")


def main():
    callSimpleLLM()


if __name__ == "__main__":
    main()
