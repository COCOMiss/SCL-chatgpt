import os
import openai
def test():
    openai.api_key = "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"
    response= openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello!"}
        ]
    )
    replay=response["choices"][0]["message"]["content"]
    print(replay)

