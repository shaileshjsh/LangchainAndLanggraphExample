# Langchain + Langgraph CLI Weather & Tips App

This project uses Langchain and Langgraph to build a CLI tool that:
- Parses user prompt for city (via Gemini LLM)
- Fetches weather data (temperature & humidity) for that city using Langchain tools
- Generates up to 5 care tips using Gemini LLM, based on weather data
- Orchestrates the flow using Langgraph nodes and edges
- Shows the final prompt sent to Gemini and the LLM’s response on the CLI

## Setup
- Python 3.9+
- Install dependencies: `pip install langchain langgraph openai google-generativeai requests python-dotenv`
- Set up your API keys in a `.env` file:
  - `OPENWEATHER_API_KEY=your_openweather_key`
  - `GOOGLE_API_KEY=your_gemini_key`

## Files
- main.py — CLI entry point, orchestrates Langgraph workflow
- weather_tool.py — Langchain tool for weather API
- llm_utils.py — Gemini LLM integration and prompt construction
- langgraph_workflow.py — Langgraph node and edge definitions
