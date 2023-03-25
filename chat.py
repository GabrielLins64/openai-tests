import openai
import os
import sys


MODEL_ENGINE = "text-davinci-003"
openai.api_key = os.environ["OPENAI_API_KEY"]


def call_chat_gpt(prompt, temperature=0.5):
    completions = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=temperature,
    )

    message = completions.choices[0].text.strip()
    return message

if __name__ == '__main__':
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if len(sys.argv) != 2:
        raise Exception("Please call this program using your question as an argument between quotes. E.g.: \"What time is it?\"")

    question = sys.argv[1]
    response = call_chat_gpt(question)
    print(response)

    # response = chat_gpt(context, model_engine)
    # print(response)