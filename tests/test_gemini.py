from llm.providers.gemini import GeminiLLM

llm = GeminiLLM()

response = llm.generate("Say hello in one sentence.")

print(response.text)
print(response.provider)
print(response.model)