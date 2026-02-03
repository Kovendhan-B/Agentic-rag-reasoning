from agents.agent import AgenticRAGAgent
from evaluation.test_cases import TEST_CASES
from evaluation.metrics import (
    retrieval_happened,
    is_refusal,
    is_grounded,
    reasoning_visible
)

agent = AgenticRAGAgent()

print("\nEVALUATION REPORT\n")

for test in TEST_CASES:
    result = agent.run(test["question"])

    report = {
        "retrieval": retrieval_happened(result),
        "refusal": is_refusal(result),
        "grounded": is_grounded(result),
        "reasoning": reasoning_visible(result)
    }

    print(
        f"{test['id']} | {test['category']} | "
        f"retrieval={report['retrieval']} | "
        f"refusal={report['refusal']} | "
        f"grounded={report['grounded']} | "
        f"reasoning={report['reasoning']}"
    )
