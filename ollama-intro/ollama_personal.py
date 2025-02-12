import requests as req
import json

# Set up the bae URL for the local Ollama API

url = "http://localhost:11434/api/chat"

# Define the payload (your input prompt)

payload = {
    "model" : "deepseek-r1",
    "messages" : [{"role" :"user", "content" : "What is the meaning of life?"}],
}

# Send the HTTP POST request with streaming enabled

response = req.post(url, json=payload, stream=True)

# Check the response status

if response.status_code == 200:
    print("Streaming response from Ollama")
    for line in response.iter_lines(decode_unicode=True):
        if line: # Ignore empty lines
            try:
                # Parse the each line as a JSON object
                json_data = json.loads(line)
                
                # Extract and print the assistant's message content
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
                    
            except json.JSONDecodeError:
                print(f"\nFailed to parse line: {line}")
                # Ensure the final output ends with a newline
    print()
    
else:
    print(f"Error: {response.status_code}")
    print(response.text)