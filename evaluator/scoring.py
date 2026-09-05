import re


def get_words(text):

    return set(
        re.findall(
            r"\b[a-zA-Z]{3,}\b",
            text.lower()
        )
    )


def similarity(response, reference):

    response_words = get_words(response)

    reference_words = get_words(reference)

    if not reference_words:

        return 0

    common_words = (
        response_words & reference_words
    )

    return len(common_words) / len(reference_words)


def score_response(response, reference):

    similarity_score = similarity(
        response,
        reference
    )

    # Accuracy
    accuracy = min(
        100,
        similarity_score * 100
    )

    # Relevance
    relevance = min(
        100,
        similarity_score * 100
    )

    # Completeness
    completeness = min(
        100,
        similarity_score * 100
    )

    # Clarity based on readable response length
    words = len(response.split())

    if words < 5:

        clarity = 40

    elif words < 15:

        clarity = 70

    elif words < 100:

        clarity = 90

    else:

        clarity = 85

    overall = (
        accuracy
        + relevance
        + clarity
        + completeness
    ) / 4

    return {

        "accuracy": round(accuracy, 2),

        "relevance": round(relevance, 2),

        "clarity": round(clarity, 2),

        "completeness": round(
            completeness,
            2
        ),

        "overall": round(
            overall,
            2
        )
    }