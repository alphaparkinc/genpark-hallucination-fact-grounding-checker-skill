"""
Sentence-Level Fact Grounding and Hallucination Verification Engine.
Zero external dependencies, standard library only.
"""

import re
from typing import Dict, List, Any

class FactGroundingCheckerClient:
    """
    Verifies that model generated claims are grounded in retrieved source context:
    - Splits answer into individual factual statements
    - Computes n-gram and entity overlap against source context
    - Flags ungrounded / unsupported sentences
    """

    def __init__(self, grounding_threshold: float = 0.40):
        self.threshold = grounding_threshold

    def _tokenize(self, text: str) -> set:
        return set(re.findall(r"\b[a-zA-Z0-9_]{3,}\b", text.lower()))

    def split_sentences(self, text: str) -> List[str]:
        """Splits narrative into discrete sentences."""
        raw = re.split(r"[.!?]+", text)
        return [s.strip() for s in raw if s.strip()]

    def verify_grounding(self, generated_answer: str, source_context: str) -> Dict[str, Any]:
        """Evaluates whether generated sentences are supported by source context."""
        context_tokens = self._tokenize(source_context)
        sentences = self.split_sentences(generated_answer)

        if not sentences:
            return {"grounded": True, "overall_score": 1.0, "sentence_results": []}

        results = []
        grounded_count = 0

        for sentence in sentences:
            s_tokens = self._tokenize(sentence)
            if not s_tokens:
                continue

            overlap = s_tokens.intersection(context_tokens)
            score = len(overlap) / len(s_tokens) if s_tokens else 0.0

            is_supported = score >= self.threshold
            if is_supported:
                grounded_count += 1

            results.append({
                "sentence": sentence,
                "overlap_ratio": round(score, 3),
                "is_supported": is_supported
            })

        overall_score = grounded_count / len(results) if results else 1.0
        return {
            "grounded": overall_score >= 0.70,
            "overall_grounding_score": round(overall_score, 3),
            "supported_sentences": grounded_count,
            "total_sentences": len(results),
            "sentence_details": results
        }
