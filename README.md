# AI-Study-Assistant-LLM

A terminal-based AI study assistant built using a locally-run Large Language Model (Llama 3.2) via Ollama. Designed to help Electrical Engineering students get quick, clear explanations of technical concepts without relying on cloud APIs.

## Features
- Runs entirely offline using a local LLM (no API key required)
- Custom system prompt tailored for EE student queries
- Simple terminal-based chat interface

## Tech Stack
- Python
- Ollama (local LLM runtime)
- Llama 3.2 (1B) model

## How it Works
The script connects to a locally running Ollama instance and sends user questions to the Llama 3.2 model with a system prompt that frames responses for an EE student audience.

## Setup
1. Install [Ollama](https://ollama.com)
2. Pull the model: `ollama pull llama3.2:1b`
3. Install dependencies: `pip install ollama`
4. Run: `python study_assistant.py`
