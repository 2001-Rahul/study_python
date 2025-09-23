import requests
import os

def api_chatbot():
    """
    A simple command-line chatbot using the Hugging Face Inference API.
    """
    # 1. Configuration
    # Replace with your Hugging Face API token
    # It's best practice to store API keys as environment variables
    HF_API_TOKEN = os.getenv("HF_API_TOKEN") 
    if not HF_API_TOKEN:
        print("Error: Hugging Face API token not found.")
        print("Please set the HF_API_TOKEN environment variable or replace 'os.getenv(\"HF_API_TOKEN\")' with your token.")
        print("You can get a token from: https://huggingface.co/settings/tokens")
        return

    # We'll use the same DialoGPT-medium model, but accessed via API
    API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

    print("Chatbot is ready! Type 'exit' to end the conversation.")
    print("Note: This chatbot communicates with the Hugging Face Inference API.")

    # 2. Initialize conversation history for the API
    # The API expects a list of dictionaries for conversation history
    conversation_history = []

    # 3. Main chat loop
    while True:
        user_input = input(">> User: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # 4. Add user input to history and prepare payload
        conversation_history.append({"role": "user", "content": user_input})
        payload = {"inputs": {"past_user_inputs": [item["content"] for item in conversation_history if item["role"] == "user"],
                              "generated_responses": [item["content"] for item in conversation_history if item["role"] == "bot"]}}

        # 5. Send request to API
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status() # Raise an exception for HTTP errors
        
        # 6. Extract and print bot's response
        bot_response = response.json()[0]["generated_text"]
        print(f"Chatbot: {bot_response}")
        conversation_history.append({"role": "bot", "content": bot_response})

if __name__ == "__main__":
    api_chatbot()