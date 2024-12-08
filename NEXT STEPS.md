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

Track git branch [step/01-simple-llm](https://github.com/rkaramc-learn/learn-llm-rag/tree/step/01-simple-llm).

## Simple LLM Enhancements

So what enhancements can we add to the simple LLM?

1. Make a reusable LLM wrapper
1. Implement logging for debugging
1. Implement timing of API calls
1. Add error handling
1. Move configuration to a config file
1. Add a prompt template
1. Stream responses
1. Cache responses
1. Support batches
1. Limit rate of API calls

In addition to the enhancements, let's also add a UI.

1. Create a web interface to the LLM
1. Format responses
1. Add interrupt/abort/retry logic
1. Support multiple LLMs
1. Monitor server health
1. Track usage and metrics

### Make A Reusable LLM Wrapper

Track git tag [step_1.1]

To make a reusable LLM wrapper, we will refactor the code in `__init__.py:callSimpleLLM()`. Extract the configuration code into a reusable function in a new file `simple_llm.py`.

### Implement Logging

Track git tag [step_1.2]

Add logging to the files `__init__.py` and `simple_llm.py`. We will be using the built-in `logging` module in Python.

Logging will help us debug the code and track usage. However, to be useful, logging will need to be at the appropriate level. For the purposes of this tutorial, we will log at the `INFO` level. Any error messages will be logged at the `ERROR` level. Common logging points are at the start and end of a function, and at the start and end of a loop or an important function call to external modules.

### Implement Timing

Track git tag [step_1.3]

Added a `Timer` class to simplify timing response from LLMs. Logs the time taken by the instrumented code.


# Version 2 -- Simple RAG

# Version 3 -- RAG Pipeline

# Version 4 -- LLM+RAG Pipeline
