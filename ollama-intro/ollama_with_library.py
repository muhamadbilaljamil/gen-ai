# conda install conda-forge::ollama 
# pip install ollama

import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "llama3.2"
prompt = "How i can start my blog to earn money?"

# Send the query to the model with streaming enabled
response = client.generate(model, prompt, stream=True)

# Print the response in a streaming manner
print("Response from Ollama:\n")

for chunk in response:
    print(chunk.response, end="", flush=True)