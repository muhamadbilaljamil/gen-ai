import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "deepseek-r1"
prompt = "What is the meaning of life?"


# Send the query from the moedl
response = client.generate(model, prompt)

# Print the response from the model

print("Response form Ollama:")
print(response.response)  # Output: "42"  # This is the response from the model