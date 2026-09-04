# SolutionsArchitect

A small Python scaffold for calling the OpenAI Chat Completions API with a reusable system
prompt. The repo name points at a larger goal (generating solutions architecture artifacts),
but the code checked in today does one thing: it holds a prompt definition in `config.py`,
sends it plus a user message to OpenAI in `gpt.py`, and prints the model's reply. The one
prompt that exists writes executive summaries of business and technical articles, with a
worked example baked in to steer the tone. Treat this as an early prototype rather than a
finished tool.

## Features

- A prompt registry in `config.py`. Each prompt is a dict with `role`, `restrictions`, and
  `examples`, concatenated into a single system message.
- A reusable OpenAI wrapper in `gpt.py` that builds the message list, calls the API, and
  appends the reply back onto the conversation.
- A command-line entry point on `gpt.py` that takes a question and a system-content string
  as positional arguments.
- A `main.py` demo that runs the executive-summary prompt against a hardcoded news article.

## Requirements

- Python 3
- An OpenAI API key exported as `OPENAI_API_KEY`. The code calls `OpenAI()` with no
  arguments, so the client reads the key from the environment.
- Packages from `requirements.txt`: `openai`, `streamlit`, `python-dotenv`.

Note: `streamlit` and `python-dotenv` are listed but not imported anywhere in the current
code. There is no Streamlit app in the repo yet, and nothing calls `load_dotenv()`, so the
key has to be present in the real shell environment.

## Installation

```bash
git clone https://github.com/espin086/SolutionsArchitect.git
cd SolutionsArchitect
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."
```

## Usage

Run the demo, which sends the executive-summary prompt and the article embedded in `main.py`:

```bash
python main.py
```

Or call `gpt.py` directly. It takes two positional arguments, the question and the system
content that defines what the model should produce:

```bash
python gpt.py "Summarize this quarter's revenue drop in two sentences." \
  "You provide executive summaries for business and technical reports."
```

```bash
python gpt.py --help
```

Output is the model's text printed to stdout. There is no file output and no logging.

## Project structure

```
.
├── config.py         Model name (GPT_MODEL = "gpt-4") and the PROMPT_EXECUTIVE_SUMMARY prompt dict
├── gpt.py            OpenAI client setup, response generation, and the argparse CLI
├── main.py           Demo script: builds the system content from config and runs one request
├── requirements.txt  openai, streamlit, python-dotenv
├── LICENSE           MIT
└── .gitignore        Standard Python ignore list
```

## How it works

`main.py` joins the `role`, `restrictions`, and `examples` fields of
`config.PROMPT_EXECUTIVE_SUMMARY` into one string and passes it to `gpt.main()` as the system
message. `gpt.main()` builds a messages list starting with that system message, creates an
OpenAI client, and hands off to `generate_response()`, which appends the user prompt, calls
`client.chat.completions.create()`, and returns the first choice's content. The reply is also
appended back to the messages list, so the structure supports multi-turn use even though
nothing loops today.

Two things in the code are inconsistent and worth knowing before you build on it:

- `config.GPT_MODEL` is set to `gpt-4`, but `gpt.py` hardcodes `gpt-3.5-turbo` in the API
  call and never reads `GPT_MODEL`.
- `main.py` passes `PROMPT_EXECUTIVE_SUMMARY["examples"]` as the `question`, not the
  `question` variable defined just above it. The article assigned to `question` is unused.

## License

MIT. See [LICENSE](LICENSE).
