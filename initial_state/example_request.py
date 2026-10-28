"""A real API example using the student's own OPENAI_API_KEY; may incur costs."""

import json

from infinite_story import get_client


def main():
    print("[Suspenseful music plays in the background]")
    client = get_client()
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "What is the capital of all countries in east africa? Reply in json where keys are countries",
            }
        ],
        model="gpt-4o-mini", # the GPT model to use
        response_format={"type": "json_object"} # we want our response in json format,
    )
    response_str = chat_completion.choices[0].message.content
    response = json.loads(response_str)
    print(response)


if __name__ == "__main__":
    main()
