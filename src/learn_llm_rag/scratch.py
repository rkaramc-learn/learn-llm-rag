class SimpleLLM:
    def __init__(self):
        self.llm = OllamaLLM(
            base_url="",
            model="",
        )

    def query(self, question):
        return self.llm.invoke(question)


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

    # Initialize Chat with remote URL and available model
    chat = ChatOllama(
        base_url="http://quark02.saury-gar.ts.net:11434",
        model="llama3.2:latest",
        format="json",
    )

    # Chat
    messages = [
        ("system", "You are a helpful researcher."),
        ("human", question),
    ]
    chat_response = chat.invoke(messages)
    print(f"A: {chat_response.join("\n")}")
