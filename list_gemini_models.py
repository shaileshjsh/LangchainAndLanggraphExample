import google.generativeai as genai

def main():
    api_key = input("Enter your Gemini API key: ").strip()
    genai.configure(api_key=api_key)
    for m in genai.list_models():
        print(m.name, m.supported_generation_methods)

if __name__ == "__main__":
    main()
