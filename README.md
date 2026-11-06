# Infinite Story - Starter Version

Read `assignment_handout.pdf` in this directory first, then complete the assignment by following Milestones 1–7.

## Set up the environment

Use Python 3.10 or newer with Tkinter. In a terminal, enter this directory, then run:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m tkinter
```

On Windows, the activation command is `.venv\Scripts\activate`. The last command should open a test window; close it once you have confirmed it works. Tkinter comes with the Python/system install and is not a package installed through pip.

## Start from the handout

```sh
python warmup.py
python infinite_story.py
```

The starter files are not fully implemented, so they will not run as a complete game. That is expected.

## API: ChatGPT or SiliconFlow

This project calls either the ChatGPT API (OpenAI) or the SiliconFlow API through the official `openai` SDK. SiliconFlow is OpenAI-compatible, so both providers share `get_client()` and `get_model()`. The project does not provide a course key, a shared key, or a free proxy. The old process in the handout for claiming a course key does not apply to this version; follow this section instead.

Milestones 1–4 do not require API calls and can be completed first. The starter code also does not create an API client on import or startup.

Before starting Milestone 5 or 7, create a key in your own OpenAI or SiliconFlow account and set it in the same terminal where you run the program.

ChatGPT, macOS / Linux:

```sh
export STORY_API_PROVIDER="openai"
export OPENAI_API_KEY="your personal API key"
python example_request.py
```

ChatGPT, Windows PowerShell:

```powershell
$env:STORY_API_PROVIDER = "openai"
$env:OPENAI_API_KEY = "your personal API key"
python example_request.py
```

SiliconFlow, macOS / Linux:

```sh
export STORY_API_PROVIDER="siliconflow"
export SILICONFLOW_API_KEY="your personal API key"
python example_request.py
```

SiliconFlow, Windows PowerShell:

```powershell
$env:STORY_API_PROVIDER = "siliconflow"
$env:SILICONFLOW_API_KEY = "your personal API key"
python example_request.py
```

If only one key is set, `STORY_API_PROVIDER` can be omitted and the code uses that provider. If both keys are set, set `STORY_API_PROVIDER` to `openai` or `siliconflow`.

`get_client()` reads the key and base URL. `get_model()` returns the default model: `gpt-4o-mini` for ChatGPT, and `Qwen/Qwen2.5-7B-Instruct` for SiliconFlow. Set `STORY_MODEL` when you want a different model. In your own code, follow `example_request.py`:

```python
client = get_client()
model = get_model()
```

That example only demonstrates an API request and JSON parsing. It does not include story generation or solutions for other milestones.

The SiliconFlow client defaults to `https://api.siliconflow.cn/v1`. For a global SiliconFlow key, point it at the matching host:

```sh
export SILICONFLOW_BASE_URL="https://api.siliconflow.com/v1"
```

Running the API example, generating new scenes, or running reflection experiments makes real API calls, billed to your own account. Check model access and usage yourself. Do not put a real key in source code, the README, screenshots, or submitted files, and do not share it with classmates. See the [OpenAI quickstart](https://developers.openai.com/api/docs/quickstart), the [Python SDK docs](https://developers.openai.com/api/reference/python), and the [SiliconFlow quickstart](https://docs.siliconflow.com/en/userguide/quickstart).

The handout covers the full requirements for the standard version, but it does not replace the local setup and API configuration notes, so keep this README as well.

You may also use other models, such as Gemini, Grok, or any model you have already purchased. However, you may override a few related code scripts if so. 

## Submission note

Do not commit anything to this repository. If you want to use GitHub for version control, create a new repository under your own account. Although the handbook mentioned the submission details, ignore that in current stage. Currently, you are not expected to submit this project and please look for further instructions if we need your submission. 
