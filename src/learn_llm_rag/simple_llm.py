from langchain_ollama import ChatOllama, OllamaLLM


def SimpleLLM():
    # Initialize LLM with remote URL and available model
    model = OllamaLLM(
        base_url="http://quark02.saury-gar.ts.net:11434",
        model="llama3.2:latest",
        format="json",
    )

    def query(question, *, llm=model):
        return llm.invoke(question)

    return query
