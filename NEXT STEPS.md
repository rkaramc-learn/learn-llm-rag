# Implementation

Build it!

## Setup Project

- Initialize project and python for a NEW project

    ```
    $ uv init --package --app                    # create a new project in <learn-llm-rag>
    $ cd learn-llm-rag
    $ uv venv                                   # setup a python virtual environment for the project
    $ source .venv/bin/activate                 # activate python virtual environment
    $ uv sync                                   # synchronize project dependencies
    $ uv install                                # install <learn_llm_rag> as an editable package
    ```

- If you are using the github.com repository,

    ```
    $ git clone https://github.com/rkaramc-learn/learn-llm-rag.git learn-llm-rag
    $ cd learn-llm-rag
    $ uv venv
    $ source .venv/bin/activate
    $ uv sync
    $ uv install
    ```

# Version 1 -- Simple LLM

- `__init__.py:callSimpleLLM()` method

    ```
    $ uv add langchain-ollama
    ```

  - Implements a very simple LLM inference flow that sends a question to the LLM
  - Pros
    - Easy to understand
    - Easy to use
    - Quick to implement
  - Cons
    - Not very reliable (responses are inconsistent)
    - Not very useful (doesn't answer the "what next?" question)
    - Not very flexible (how do add features to this without making it complex?)
    - Not very scalable (can't be modifying code every time the question changes)
    - Not very robust (no error handling)
    - Not very efficient (spends most of its time waiting for the LLM to respond)

  So in effect, this is only a "toy" implementation.
