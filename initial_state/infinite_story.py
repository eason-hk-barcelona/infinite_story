import json
import os

from graphics import Canvas
from openai import OpenAI

STORY_NAME = "original_small"


def get_client():
    """API setup only: each student uses their own environment-variable key."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Set your own OPENAI_API_KEY in the terminal before calling the API. "
            "Do not put your API key in the source code."
        )
    return OpenAI(api_key=api_key, base_url="https://api.openai.com/v1")


def main():
    print("Infinite Story")
    # TODO: your code here


if __name__ == "__main__":
    main()
