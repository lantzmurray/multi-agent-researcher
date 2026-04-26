"""
Fact-Checker Agent - Reviews summaries for hallucinations, bias, or gaps.

This agent reviews the summarized content for potential issues such as:
- Hallucinated facts (unverifiable claims)
- Bias in presentation
- Missing context or important considerations
"""

from agents.base import call_llm


def fact_check(text: str) -> str:
    """
    Review the provided text for accuracy and potential issues.

    Args:
        text: The summarized text to fact-check

    Returns:
        Feedback on the text including potential issues and suggestions
    """
    prompt = (
        "Review the following summary for bias, hallucinations, or gaps. "
        "Provide specific feedback on:\n"
        "1. Any claims that seem exaggerated or unverifiable\n"
        "2. Potential bias in the presentation\n"
        "3. Missing context or important considerations\n"
        "4. Suggestions for improvement\n\n"
        f"Summary to review:\n{text}"
    )

    return call_llm(prompt)
