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

### Error Handling

Track git tag [step_1.4]

**What are the errors that can be expected?**

- Reviewing the code, we can identify the following categories of errors:

    - Configuration errors
    - Network errors
    - Query errors
    - Response errors

The simplest way to handle errors is to catch any exceptions raised at the top level, log them and return a default response.
The try..catch in `__init__.py:callSimpleLLM()` is not the best way to handle errors, but it will do for a first step (see code marked `# [Step 1.4a]`).

The next step is to add a more specific error handler for each type of error.

Configuration errors should occur when configuring the LLM as the configuration values are tested for validity -- in `simple_llm.py:SimpleLLM()`. 
This is not the case for `langchain` models like `OllamaLLM`, because the model object creation does not validate configuration values. 
The model object initialization serves only to capture configuration values. 
Therefore, error handling at this stage becomes a matter of ensuring that the configuration values are valid **prior to** initializing the model object.

- **base_url** is the server URL for the LLM. Validating this is a matter of ensuring that it is a valid URL, and that the LLM is active and responding at this URL.
- **model_name** is the name of the model to use. To validate this, we need to ensure the model is available at the `base_url`.

See code marked `# [Step 1.4b]`.

Network and Query errors occur when querying the LLM -- in `simple_llm.py:SimpleLLM.query()`.

Response errors occur when reading the response from the LLM -- in `__init__.py:callSimpleLLM()`. This is especially important when using streaming responses.

The existing logging statements take care of network, query and response errors. For a simple one-shot LLM wrapper, all we need to do is log the error and return a default response. More extensive error handling will be required when building a UI for the LLM.

### Move Configuration to a Config File

Configuration values should be moved to a separate config file. This will make it easier for us to change the configuration and the code independently. The code also becomes more reusable and testable.

The simplest approach is to hold all the required configuration values in the OS shell environment. To set these environment variables, we can use the python-dotenv package.

- Install the python-dotenv package using `uv add python-dotenv`
- Create a `.env` file in the project root directory
- Add the required configuration values to the `.env` file
- Load the configuration values from the `.env` file using the python-dotenv package

Since the `.env` file may contain sensitive information, do not commit this to the repository. To assure this, remember to add the `.env` file to the `.gitignore` file if it is not already there.

See code marked `# [Step 1.4c]`.

There are alternatives to environment variables and the python-dotenv package. These include:

- Command line arguments

    We can use command line arguments to pass configuration values to the program, but this method is used most often to supplement and/or override the configuration values in the `.env` file. We will eventually build a command line interface in the tutorial.

- INI/YAML/JSON/TOML files

    The configuration file options are in many cases more flexible and powerful, but they are also more complex to configure and use. The environment variables approach is the most common and most simple to use. We will move to other alternatives only if we need their flexibility and expressive power.

### Add a Prompt Template

A `Prompt` is the input to the LLM. In the simplest case, the prompt is the same as the user's query. The LLM's response is generated based on the prompt provided, so if the query is worded correctly, the response will also be reasonably accurate. Depending on the user's intent, a more detailed query will result in a better response. Since the LLM is a probabilistic model, certain types of prompts tend to generate better responses. These include specific instructions and guidelines for the LLM that channel the model's natural language processing capabilities to function better.

The `Prompt Template` includes these guidelines and instructions, in addition to the user's query, without requiring the user to provide this on every interaction. The template is an aid for the user to make the query more specific, and thereby improving the quality of the response.

    - Example of a Prompt Template:
        ```
        You are a helpful, respectful, and honest assistant.
        Follow a chain-of-thoughts format when generating the response.

        Question: {question}

        Answer: Let's think step by step.
        ```

See the [Prompt Engineering Guide](https://www.promptingguide.ai/) for more information on this topic.

We will implement a prompt template as an input to the LLM wrapper. See code marked `# [Step 1.4d]`.

### Make a Reusable LLM Wrapper Class

We will refactor the `SimpleLLM` function to return an instance of new class called `OllamaLLMServer`. Currently, `SimpleLLM` returns a query function, but by changing it to return a class instance, we can more easily add functionality in the future. The `OllamaLLMServer` class will serve as a reusable wrapper for interacting with the Ollama LLM server, encapsulating the query functionality and allowing for easier expansion of features.

### Stream the Response

Till now, we have been displaying the response from the LLM server once the full response has been received. This approach is simple, but is not ideal for the user experience.

Users perceive the below issues when they are waiting for a response from the LLM server:

- **Lack of interactivity** causes users problems when trying to interrupt or cancel the query. In addition, users may be unable to react to the content till it is completely downloaded and/or displayed.

- **Limited context switching**, that is continuing with other tasks while waiting for the response, is not possible for the user as they wait for the full response to be downloaded.

- **Frustration with errors** arises when the LLM server is unable to generate a correct response after having waited for a long time.

- **Long wait times** cause users to experience significant delays before seeing the output, especially for long responses. **Timeout issues** due to network delays or errors makes this worse as the full response is lost due to these errors. The **perceived slowness** of the application frustrates users and reduces their engagement with the application.

Adding streaming capability to LLM responses is therefore an important feature. Streaming allows the user to see the response as it is generated, thus providing a more responsive and engaging experience. The above issues are mitigated to an extent with streaming, provided it is implemented correctly.

For this tutorial, we will implement streaming capabilities in the `OllamaLLMServer` class by adding a method `query_with_stream()`.

### Cache the Response

Caching responses from the LLM can speed up the application for users, while reducing the number of calls made to the LLM server. To make the best use of caching, first review the queries being sent to the LLM, and the responses being returned. Where the queries are worded the same, and if the responses expected from the LLM are the same, then caching makes sense. If any of these conditions are not met, then caching should not be used.

In this tutorial, we will implement caching in the `OllamaLLMServer` class by adding an argument `cache=True` to `OllamaLLMServer()` in `SimpleLLM()`. To trigger this, set an environment variable `LLM_CACHE_MODE` to `true` in the `.env` file.

To demonstrate caching, we will run the prompt three times in `callSimpleLLM()`.

NOTE: Caching is currently not supported for the `OllamaLLM` class in `langchain-ollama` package. See the [langchain issue](https://github.com/langchain-ai/langchain/issues/25712) for more information.

We will retry this in subsequent tutorial steps.

# Version 2 -- Simple RAG

# Version 3 -- RAG Pipeline

# Version 4 -- LLM+RAG Pipeline
