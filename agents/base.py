"""Shared Ollama helper for Project 11's LLM-backed agents."""

import requests
import json

# Project 11 can run for a while on this Intel Mac, so use a long read timeout.
OLLAMA_TIMEOUT_SECONDS = 1800

OLLAMA_API_URL = "http://localhost:11434/api/generate"


def _read_ollama_stream(response: requests.Response) -> str:
    """Read Ollama's streamed NDJSON chunks into one response string."""
    chunks = []
    for line in response.iter_lines(decode_unicode=True):
        if not line:
            continue
        data = json.loads(line)
        chunks.append(data.get("response", ""))
        if data.get("done"):
            break
    return "".join(chunks).strip()


def call_llm(prompt: str, model: str = "llama2") -> str:
    """Send a prompt to Ollama with a Mac-friendly timeout window."""
    with requests.post(
        OLLAMA_API_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": True,
        },
        timeout=(10, OLLAMA_TIMEOUT_SECONDS),
        stream=True,
    ) as response:
        response.raise_for_status()
        return _read_ollama_stream(response)
