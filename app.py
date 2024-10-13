from flask import Flask, request, jsonify
from mistralai import Mistral
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the API key from environment variables
api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    # Call the Mistral AI API
    chat_response = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {
                "role": "user",
                "content": user_message,
            },
        ]
    )

    # Extract the assistant's reply
    assistant_reply = chat_response.choices[0].message.content

    return jsonify({'reply': assistant_reply})

if __name__ == '__main__':
    app.run(debug=True)
