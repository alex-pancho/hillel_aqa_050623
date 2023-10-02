#!/bin/env python
import requests
import json
from config import API_KEY


def send_message(message):
    """
    Sends a user message to the Chat GPT API and receives a model-generated response.

    Args:
        message (str): The user message.

    Returns:
        str: The model-generated response.
    """
    endpoint = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                     {'role': 'user', 'content': message}]
    }

    response = requests.post(endpoint, headers=headers, json=data)
    response_data = json.loads(response.text)
    model_reply = response_data['choices'][0]['message']['content']

    return model_reply


# Example usage
user_input = input("You: ")

while user_input.lower() != 'exit':
    rsp = send_message(user_input)
    print("ChatGPT:", rsp)

    user_input = input("You: ")
