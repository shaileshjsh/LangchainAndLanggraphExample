from langgraph.graph import StateGraph, END
from weather_tool import get_weather
from llm_utils import extract_city_from_prompt, generate_care_tips, get_gemini_llm

# Node 1: City input (parse city from user prompt)
def city_input_node(state):
    prompt = state["user_prompt"]
    api_key = state["gemini_api_key"]
    llm = get_gemini_llm(api_key)
    city = extract_city_from_prompt(prompt, llm=llm)
    return {"city": city, **state}

# Node 2: Temperature retrieval
def temperature_node(state):
    city = state["city"]
    weather = get_weather(city)
    return {"temperature": weather["temperature"], **state}

# Node 3: Care tips generation
def tips_node(state):
    city = state["city"]
    temp = state["temperature"]
    api_key = state["gemini_api_key"]
    llm = get_gemini_llm(api_key)
    final_prompt, tips = generate_care_tips(city, temp, llm=llm)
    return {"final_prompt": final_prompt, "tips": tips, **state}

def build_workflow():
    graph = StateGraph(dict)
    graph.add_node("city_input", city_input_node)
    graph.add_node("temperature", temperature_node)
    graph.add_node("tips", tips_node)
    from langgraph.graph import START
    graph.add_edge(START, "city_input")
    graph.add_edge("city_input", "temperature")
    graph.add_edge("temperature", "tips")
    graph.add_edge("tips", END)
    return graph
