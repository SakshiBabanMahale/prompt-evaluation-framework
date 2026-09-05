# Prompt Evaluation Framework

A simple Python framework to compare multiple prompt templates automatically.

## Features
- Multiple prompt templates
- Configurable test cases
- Automatic LLM-based scoring
- Accuracy, relevance, clarity, completeness
- Response latency and token usage tracking
- JSON evaluation results
- Markdown evaluation report
- CLI interface

## Setup

```bash
python -m venv env
# Windows
env\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

Run:

```bash
python main.py
```

The report is generated in `reports/evaluation_report.md`.

## Offline demo

If no API key is configured, the project runs in demo mode using deterministic mock responses so the complete workflow can be tested.
