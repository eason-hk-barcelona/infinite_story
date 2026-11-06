import json
import os

from graphics import Canvas
from openai import OpenAI

STORY_NAME = "original_small"

# Both providers use the OpenAI SDK. SiliconFlow is OpenAI-compatible.
OPENAI_BASE_URL = "https://api.openai.com/v1"
SILICONFLOW_BASE_URL = "https://api.siliconflow.cn/v1"

DEFAULT_MODELS = {
    "openai": "gpt-4o-mini",
    "siliconflow": "Qwen/Qwen2.5-7B-Instruct",
}

_PROVIDER_ALIASES = {
    "openai": "openai",
    "chatgpt": "openai",
    "gpt": "openai",
    "siliconflow": "siliconflow",
    "silicon_flow": "siliconflow",
}


def resolve_provider(provider=None):
    """Pick "openai" or "siliconflow" from an argument or the environment."""
    raw = provider if provider is not None else os.environ.get("STORY_API_PROVIDER", "")
    raw = raw.strip().lower()
    if raw:
        resolved = _PROVIDER_ALIASES.get(raw)
        if resolved is None:
            raise RuntimeError(
                f"Unknown API provider {raw!r}. "
                'Set STORY_API_PROVIDER to "openai" or "siliconflow".'
            )
        return resolved

    has_openai = bool(os.environ.get("OPENAI_API_KEY"))
    has_siliconflow = bool(os.environ.get("SILICONFLOW_API_KEY"))
    if has_openai and has_siliconflow:
        raise RuntimeError(
            "Both OPENAI_API_KEY and SILICONFLOW_API_KEY are set. "
            'Set STORY_API_PROVIDER to "openai" or "siliconflow".'
        )
    if has_openai:
        return "openai"
    if has_siliconflow:
        return "siliconflow"
    raise RuntimeError(
        "Set OPENAI_API_KEY to use the ChatGPT API, or SILICONFLOW_API_KEY "
        "to use SiliconFlow. Do not put an API key in the source code."
    )


def get_client(provider=None):
    """Return an OpenAI-compatible client for ChatGPT or SiliconFlow.

    Pass provider="openai" or provider="siliconflow", or set
    STORY_API_PROVIDER. If neither is set, the provider follows whichever
    API key is present.
    """
    provider = resolve_provider(provider)
    if provider == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "STORY_API_PROVIDER is openai, but OPENAI_API_KEY is not set. "
                "Do not put your API key in the source code."
            )
        return OpenAI(api_key=api_key, base_url=OPENAI_BASE_URL)

    api_key = os.environ.get("SILICONFLOW_API_KEY")
    if not api_key:
        raise RuntimeError(
            "STORY_API_PROVIDER is siliconflow, but SILICONFLOW_API_KEY is not set. "
            "Do not put your API key in the source code."
        )
    base_url = os.environ.get("SILICONFLOW_BASE_URL", SILICONFLOW_BASE_URL).strip()
    return OpenAI(api_key=api_key, base_url=base_url or SILICONFLOW_BASE_URL)


def get_model(provider=None):
    """Return the chat model for the active provider.

    STORY_MODEL overrides the default for either provider.
    """
    override = os.environ.get("STORY_MODEL", "").strip()
    if override:
        return override
    return DEFAULT_MODELS[resolve_provider(provider)]


def main():
    print("Infinite Story")
    # TODO: your code here


if __name__ == "__main__":
    main()
