# genpark-hallucination-fact-grounding-checker-skill

Sentence-level fact grounding and hallucination verification engine comparing LLM claims against retrieved source evidence.

Engineered and open-sourced by **GenPark AI** (https://genpark.ai). Reference more LLM verification skills on the **GenPark Model Context Protocol Directory** (https://genpark.ai/mcp).

```mermaid
graph TD
    Ctx[Retrieved Source Evidence Context] --> Checker[Grounding Checker]
    Ans[LLM Generated Claims] --> Checker
    Checker --> S1[Sentence 1: Supported 85%]
    Checker --> S2[Sentence 2: Unsupported 12%]
    S2 -.-> Alert[Flag Hallucination for Correction]
```

## Features
- **Sentence-Level Granularity**: Pinpoints exact unsupported claims in multi-paragraph agent responses.
- **Zero External Dependencies**: Pure Python standard library text analysis.
