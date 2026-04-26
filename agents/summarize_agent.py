"""
Summarizer Agent - Condenses findings into concise insights.

This agent takes raw search results and condenses them into
3-5 bullet points for easy consumption. Uses LLaMA 2 via Ollama.
"""

from agents.base import call_llm


def summarize_text(text: str) -> str:
    """
    Summarize the provided text into key bullet points.

    Args:
        text: Raw text to summarize (usually search results)

    Returns:
        A concise summary in bullet point format
    """
    prompt = f"Summarize the following findings in 3-5 bullet points:\n\n{text}"

    return call_llm(prompt)
