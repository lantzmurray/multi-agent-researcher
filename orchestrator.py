"""
Orchestrator - Coordinates the multi-agent research pipeline.

This module orchestrates the workflow between:
1. Search Agent - Collects raw information
2. Summarizer Agent - Condenses findings
3. Fact-Checker Agent - Reviews for accuracy
4. Report Generator Agent - Produces final report

The orchestrator manages data flow between agents and returns
a comprehensive result dictionary.
"""

from agents.search_agent import run_search
from agents.summarize_agent import summarize_text
from agents.checker_agent import fact_check
from agents.report_agent import generate_report


def run_research_pipeline(topic: str) -> dict:
    """
    Run the full multi-agent research pipeline for a topic.

    Args:
        topic: The research topic to investigate

    Returns:
        Dictionary containing:
        - search: Raw search results
        - summary: Condensed summary
        - corrections: Fact-checker feedback
        - report: Final polished report
    """
    search_results = run_search(topic)
    summary = summarize_text(search_results)
    corrections = fact_check(summary)
    report = generate_report(summary, corrections)

    return {
        "search": search_results,
        "summary": summary,
        "corrections": corrections,
        "report": report
    }