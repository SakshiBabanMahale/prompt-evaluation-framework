def generate_report(results):

    lines = [

        "# Prompt Evaluation Report",

        "",

        "## Prompt Comparison",

        "",

        "| Rank | Prompt | Accuracy | Relevance | Clarity | Completeness | Overall |",

        "|---:|---|---:|---:|---:|---:|---:|"
    ]

    for i, result in enumerate(results, 1):

        s = result["average_scores"]

        lines.append(

            f"| {i} | "
            f"{result['prompt_name']} | "
            f"{s['accuracy']}% | "
            f"{s['relevance']}% | "
            f"{s['clarity']}% | "
            f"{s['completeness']}% | "
            f"**{s['overall']}%** |"
        )

    winner = results[0]

    # Detect mode
    modes = []

    for result in results:

        for case in result["cases"]:

            modes.append(case["mode"])

    if "REAL LLM" in modes:

        evaluation_mode = "REAL LLM MODE"

    else:

        evaluation_mode = "DEMO MODE"

    lines += [

        "",

        "## Evaluation Mode",

        "",

        f"**{evaluation_mode}**",

        ""
    ]

    if evaluation_mode == "DEMO MODE":

        lines += [

            "> No LLM API was available. "
            "The framework automatically used "
            "Demo Mode so the complete evaluation "
            "pipeline could still be tested.",

            ""
        ]

    else:

        lines += [

            "> Responses were generated using "
            "the configured LLM API.",

            ""
        ]

    lines += [

        "## Best Prompt",

        "",

        f"**{winner['prompt_name']}** achieved "
        f"the highest overall score of "
        f"**{winner['average_scores']['overall']}%**.",

        "",

        "## Detailed Results",

        ""
    ]

    for result in results:

        lines.append(
            f"### {result['prompt_name']}"
        )

        lines.append("")

        for case in result["cases"]:

            lines.append(
                f"**{case['test_case_id']}** — "
                f"{case['input']}"
            )

            lines.append("")

            response = (
                case["response"]
                .replace("\n", " ")
            )

            lines.append(
                f"> {response}"
            )

            lines.append("")

            lines.append(

                f"Mode: **{case['mode']}** | "
                f"Overall: **"
                f"{case['scores']['overall']}%** | "
                f"Latency: "
                f"{case['latency_seconds']}s | "
                f"Tokens: "
                f"{case['tokens']}"
            )

            lines.append("")

    return "\n".join(lines)