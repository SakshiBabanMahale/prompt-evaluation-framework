# Prompt Evaluation Framework

An AI-based tool that compares different prompts, evaluates their responses, and helps identify the most effective prompt.

## Features

* Compare multiple prompt templates
* Generate responses using OpenAI
* Evaluate response quality
* Measure accuracy, relevance, clarity, and completeness
* Calculate overall scores
* Rank prompts based on performance
* Generate evaluation reports
* Supports Demo Mode when the API is unavailable

## How It Works

```text
Test Question
      ↓
Multiple Prompts
      ↓
OpenAI
      ↓
Generated Responses
      ↓
Evaluation
      ↓
Accuracy / Relevance / Clarity / Completeness
      ↓
Prompt Ranking
      ↓
Best Prompt
```

## Technologies Used

* Python
* OpenAI API
* python-dotenv
* JSON
* Git & GitHub

## Project Structure

```text
prompt-evaluation-framework/
│
├── data/
│   └── test_cases.json
│
├── evaluator/
│   ├── __init__.py
│   ├── llm.py
│   ├── runner.py
│   ├── scoring.py
│   └── report.py
│
├── reports/
│   └── evaluation_report.md
│
├── templates/
│   └── prompts.json
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/SakshiBabanMahale/prompt-evaluation-framework.git
```

Open the project folder:

```bash
cd prompt-evaluation-framework
```

Create a virtual environment:

```bash
python -m venv env
```

Activate it on Windows:

```powershell
.\env\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## API Key Setup

Create a `.env` file in the project folder:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

Replace `your_openai_api_key_here` with your OpenAI API key.

**Never upload your `.env` file or API key to GitHub.**

## Run the Project

Run:

```bash
python main.py
```

The framework will generate responses, evaluate them, compare the prompts, and create an evaluation report.

## Output

The evaluation results are stored in:

```text
data/results.json
```

The evaluation report is generated in:

```text
reports/evaluation_report.md
```

## Demo Mode

If an OpenAI API key is not available or the API request fails, the framework automatically switches to Demo Mode so that the project can still run.

## Future Improvements

* LLM-as-a-Judge evaluation
* More evaluation metrics
* Web-based dashboard
* Support for multiple LLM providers
* Visualization of prompt performance
* Advanced prompt optimization

## Author

**Sakshi Baban Mahale**

GitHub: https://github.com/SakshiBabanMahale
