
import ollama # type: ignore

# Define the model name (use a lightweight model like "mistral" or  ollama pull tinyllama:1.1b)
model_name = "tinyllama:1.1b"
# Define the user input prompt
prompt = input( "Enter your prompt: ")
# Run the model and get a response
response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
# Print the response
print("AI Response:", response["message"]["content"])
