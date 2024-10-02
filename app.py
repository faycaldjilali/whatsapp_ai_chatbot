from flask import Flask, request
import cohere
from twilio.twiml.messaging_response import MessagingResponse
import os

# Init the Flask App
app = Flask(__name__)

# Initialize Cohere API key
cohere_client = cohere.Client('your-api-key')

# Function to generate a response using Cohere with the custom prompt
def generate_cohere_answer(question):
    prompt = (f"Q: {question}\n"
              "A: Please provide a detailed and comprehensive answer explaining the concept in depth.\n")

    response = cohere_client.generate(
        model='command-r-plus-08-2024',
        prompt=prompt,
        max_tokens=300,  # You can adjust the token limit as needed
        temperature=0.7,  # Control randomness in generation
    )

    answer = response.generations[0].text.strip()
    return answer

# Define a route to handle incoming requests from Twilio WhatsApp
@app.route('/cohere', methods=['POST'])
def cohere_route():
    incoming_msg = request.values.get('Body', '').lower()
    print("Incoming Message: ", incoming_msg)

    # Use Cohere to generate an answer with the custom prompt
    response_text = generate_cohere_answer(incoming_msg)

    print("Bot Response: ", response_text)
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    msg.body(response_text)
    return str(bot_resp)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
@app.route('/')
def home():
    return "Welcome to the local Flask app!"
