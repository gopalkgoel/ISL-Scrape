from openai import OpenAI
import json

with open("secret_keys.json", "r") as json_file:
    secret_keys = json.load(json_file)

client = OpenAI(
        api_key=secret_keys["api_key"],  
        project=secret_keys["project"],
        )

def LLM(system_prompt="You are a helpful assistant.", user_prompt="Hi!"):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
    )

    return completion.choices[0].message.content