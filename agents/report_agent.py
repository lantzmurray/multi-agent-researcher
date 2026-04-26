"""
Report Generator Agent - Produces a polished final research brief.

This agent takes the summary and fact-checker feedback to produce
a polished, executive-ready research report. Uses LLaMA 2 via Ollama.
"""

from agents.base import call_llm


def generate_report(summary: str, corrections: str) -> str:
    """
    Generate a polished research report from summary and corrections.

    Args:
        summary: The condensed summary from the summarizer agent
        corrections: Feedback from the fact-checker agent

    Returns:
        A polished executive-style research report
    """
    prompt = f"""
Using the summary and fact-checker feedback below, write a polished research report.

The report should include:
1. Executive Summary (2-3 sentences)
2. Key Findings (bullet points)
3. Considerations & Recommendations
4. Conclusion

Summary:
{summary}

Fact-Checker Feedback:
{corrections}
"""

    return call_llm(prompt)
