<h2>OpenAI API tests</h2>

Repository intended to test the OpenAI Algorithms through its API.

---

<h2>Index</h2>

- [Installing OpenAI API](#installing-openai-api)
- [How to get an OpenAPI Key](#how-to-get-an-openapi-key)

---

#### Installing OpenAI API

First, create and activate your Python Virtual Environment:

```shell
python -m venv venv
. venv/bin/activate
```

Then, install the openai API:

```shell
pip install openai
```

#### How to get an OpenAPI Key

To use the OpenAI API, you will need to have an OpenAI API key. Here's how you can get one:

Go to the OpenAI website (https://openai.com/) and click on the "Sign up for the API" button at the top right of the page.

Enter your email address and follow the prompts to create an account. If you already have an OpenAI account, skip this step.

Once you've created an account, go to the API dashboard (https://platform.openai.com/overview) and click on "Personal", then "View API keys".

Click on the "Create new API key" button and follow the prompts to generate a new API key.

Copy the API key and save it somewhere secure, as you'll need it to authenticate your requests to the OpenAI API.

Set the OPENAI_API_KEY environment variable to your API key in the command line or in your project's configuration file. For example, you can use the following command in your terminal:

```shell
export OPENAI_API_KEY=<your-api-key>
```

With your API key set up as an environment variable, you should be able to make requests to the OpenAI API. Be sure to check the OpenAI API documentation (https://beta.openai.com/docs/api-reference/introduction) for more information on how to use the API and the available endpoints.