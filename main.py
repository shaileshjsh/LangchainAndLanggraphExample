
import sys
from langgraph_workflow import build_workflow
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    gemini_api_key = os.getenv("GOOGLE_API_KEY")
    weather_api_key = os.getenv("GOOGLE_WEATHER_API_KEY")
    if len(sys.argv) > 1:
        user_prompt = " ".join(sys.argv[1:])
    else:
        print("Enter your prompt (e.g., 'How should I care for myself in Mumbai today?'):")
        user_prompt = input().strip()
    workflow = build_workflow()
    app = workflow.compile()
    state = {"user_prompt": user_prompt, "gemini_api_key": gemini_api_key, "weather_api_key": weather_api_key}
    result = app.invoke(state)
    print("\n--- Final Prompt to LLM ---\n")
    print(result.get("final_prompt", "N/A"))
    print("\n--- LLM Response (Care Tips) ---\n")
    print(result.get("tips", "N/A"))

if __name__ == "__main__":
    main()
