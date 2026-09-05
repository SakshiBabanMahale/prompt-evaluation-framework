import json

from .llm import generate_response
from .scoring import score_response


def load_prompts():

    with open(
        "templates/prompts.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def evaluate_all(test_cases):

    prompts = load_prompts()

    results = []

    for prompt_info in prompts:

        prompt_scores = []

        for case in test_cases:

            prompt = prompt_info["template"].format(
                input=case["input"]
            )

            # Generate response
            result = generate_response(prompt)

            response = result["response"]

            latency = result["latency"]

            tokens = result["tokens"]

            mode = result["mode"]

            # Evaluate response
            scores = score_response(
                response,
                case["reference"]
            )

            prompt_scores.append({

                "test_case_id": case["id"],

                "input": case["input"],

                "response": response,

                "latency_seconds": latency,

                "tokens": tokens,

                "mode": mode,

                "scores": scores
            })

        # Calculate averages
        avg = {}

        for metric in [
            "accuracy",
            "relevance",
            "clarity",
            "completeness",
            "overall"
        ]:

            avg[metric] = round(
                sum(
                    x["scores"][metric]
                    for x in prompt_scores
                )
                / len(prompt_scores),
                2
            )

        results.append({

            "prompt_id": prompt_info["id"],

            "prompt_name": prompt_info["name"],

            "average_scores": avg,

            "cases": prompt_scores
        })

    # Highest score first
    results.sort(
        key=lambda x:
        x["average_scores"]["overall"],
        reverse=True
    )

    return results