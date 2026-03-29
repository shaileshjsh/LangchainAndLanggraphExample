
import google.generativeai as genai


def get_gemini_llm(api_key):
    if not api_key:
        raise ValueError("Gemini API key must be provided.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("models/gemini-2.5-flash")

def extract_city_from_prompt(prompt: str, llm=None) -> str:
    """
    Use Gemini LLM to extract city name from user prompt.
    """
    if llm is None:
        raise ValueError("LLM instance must be provided with API key.")
    system_prompt = (
        "Extract the city name from the following prompt. "
        "If no city is found, respond with 'UNKNOWN'.\nPrompt: " + prompt
    )
    response = llm.generate_content(system_prompt)
    return response.text.strip()

def generate_care_tips(city: str, temperature: float, llm=None) -> (str, str):
    """
    Use Gemini LLM to generate up to 5 care tips based on temperature.
    Returns (final_prompt, llm_response)
    """
    if llm is None:
        raise ValueError("LLM instance must be provided with API key.")
    final_prompt = (
        f"Given that the temperature in {city} is {temperature}°C, "
        "suggest up to 5 care tips for someone in {city}. Each tip should be a single sentence."
    )
    response = llm.generate_content(final_prompt)
    return final_prompt, response.text.strip()
