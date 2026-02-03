def retrieval_happened(result):
    return len(result.get("sources", [])) > 0


def is_refusal(result):
    refusal_markers = [
        "could not find",
        "cannot answer",
        "insufficient",
        "does not contain"
    ]
    answer = result.get("answer", "").lower()
    return any(marker in answer for marker in refusal_markers)


def is_grounded(result):
    sources = result.get("sources", [])
    if not sources:
        return False

    answer = result.get("answer", "").lower()
    source_text = " ".join(s["text"].lower() for s in sources)

    return any(sentence.strip() in source_text for sentence in answer.split("."))


def reasoning_visible(result):
    return len(result.get("thoughts", [])) >= 2
