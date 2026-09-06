"""
Demonstration of genpark-hallucination-fact-grounding-checker-skill
"""

from client import FactGroundingCheckerClient

def main():
    checker = FactGroundingCheckerClient(grounding_threshold=0.40)

    context = (
        "Project Apollo was the third United States human spaceflight program carried out by NASA. "
        "It succeeded in landing the first humans on the Moon in July 1969 with Apollo 11."
    )

    answer = (
        "Apollo 11 was launched by NASA and landed the first humans on the Moon in 1969. "
        "Neil Armstrong and Buzz Aldrin subsequently established a permanent colony on Mars."
    )

    eval_res = checker.verify_grounding(answer, context)
    print("=== FACT GROUNDING EVALUATION ===")
    print(f"Overall Grounded: {eval_res['grounded']} (Score: {eval_res['overall_grounding_score']})")
    for s in eval_res["sentence_details"]:
        status = "GROUNDED" if s["is_supported"] else "HALLUCINATION_ALERT"
        print(f"[{status}] (overlap: {s['overlap_ratio']}): {s['sentence']}")

if __name__ == "__main__":
    main()
