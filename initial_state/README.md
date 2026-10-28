# Infinite Story - 学生初始版

先阅读本目录的 `assignment_handout.pdf`，按 Milestone 1-7 完成作业。

## 这份代码的起点

- 基于 Stanford 官方 `starter_code.zip`，仅将 API 接入改为学生自己的 OpenAI API；`infinite_story.py` 仍是没有 milestone 答案的起始代码。
- `infinite_ethics.txt`、`graphics.py` 和 `data/` 保持官方原始内容。
- 官方 ZIP 没有 `warmup.py`，这里补了一个无答案的空白入口，供 Milestone 1 使用。
- `img/` 保留官方的 58 张图片，并加入之前补齐的 17 张图片，共 75 张；新增图片不包含解题代码。
- 只保留普通版作业需要的文件，不包含 lite 版。

项目官方页面：https://nifty.stanford.edu/2025/piech-infinite-story/

## 准备环境

使用带 Tkinter 的 Python 3.10 或更新版本。在终端进入本目录，然后运行：

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m tkinter
```

Windows 激活命令为 `.venv\Scripts\activate`。最后一个命令应打开测试窗口；确认后关闭即可。Tkinter 随 Python/系统安装，不是通过 pip 安装的包。

## 按 handout 开始

```sh
python warmup.py
python infinite_story.py
```

初始文件没有完成实现，因此不会直接运行出完整游戏，这是正常的。

## API：每位学生使用自己的 OpenAI 密钥

本项目直接使用官方 `openai` SDK，不提供学校的课程密钥、共享密钥或免费中转服务。handout 中领取课程密钥的旧流程不适用于本版本，以本节为准。

Milestone 1-4 不需要调用 API，可以先完成；起始代码也不会在导入或启动时创建 API 客户端。

开始 Milestone 5 或 7 前，请在自己的 OpenAI 账户创建 API key，确认账户可用，并在运行程序的同一终端设置 `OPENAI_API_KEY`。例如，macOS / Linux：

```sh
export OPENAI_API_KEY="你的个人 API key"
python example_request.py
```

Windows PowerShell：

```powershell
$env:OPENAI_API_KEY = "你的个人 API key"
python example_request.py
```

`get_client()` 已负责从环境变量读取密钥；需要调用 API 时使用 `client = get_client()`，参照 `example_request.py`。该示例只演示 API 请求与 JSON 解析，不包含剧情生成或其他 milestone 的解答。

示例使用 `gpt-4o-mini` 模型。运行 API 示例、生成新场景或进行反思实验会真实调用 API，由学生自己的账户承担费用；请自行检查模型访问权限和用量。不要将真实密钥写入源码、README、截图或提交文件，也不要分享给同学。详见 [OpenAI 官方入门文档](https://developers.openai.com/api/docs/quickstart) 和 [Python SDK 文档](https://developers.openai.com/api/reference/python)。

handout 已覆盖完整普通版的任务要求，但不能替代本地环境安装和 API 配置说明，所以请同时保留本 README。

## 提交

按 handout 提交 `warmup.py`、`infinite_story.py`、`infinite_ethics.txt`，以及扩展功能必需的文件。不要提交 API 密钥或 `.venv/`。
