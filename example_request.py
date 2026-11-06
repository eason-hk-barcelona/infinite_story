"""A real API example using ChatGPT or SiliconFlow; may incur costs."""

import json

from infinite_story import get_client, get_model


def main():
    print("[Suspenseful music plays in the background]")
    client = get_client()
    model = get_model()
    print(f"Using model: {model}")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "What is the capital of all countries in east africa? Reply in json where keys are countries",
            }
        ],
        model=model,
        response_format={"type": "json_object"},  # we want our response in json format
    )
    response_str = chat_completion.choices[0].message.content
    response = json.loads(response_str)
    print(response)


if __name__ == "__main__":
    main()
