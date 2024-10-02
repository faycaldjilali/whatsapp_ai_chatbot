# whatsapp_ai_chatbot
Create a Twilio Account

"Go to Twilio and sign up for an account if you don't already have one.
Once logged in, navigate to the Messaging section.
Select WhatsApp messaging from the menu."

2. Get a WhatsApp-Enabled Twilio Number

    Twilio will provide a WhatsApp-enabled phone number.
    Save this number as a contact in your phone (you'll need it to send and receive messages).

3. Copy the Twilio Verification Code

    In the Twilio console, you will see a verification code.
    Send this code to your WhatsApp-enabled Twilio number from your WhatsApp chat.

4. Install the Required Python Libraries

    In your terminal, run the following command to install the necessary libraries:

    bash

   ** pip install -r requirements.txt**

5. Add Your Twilio API Keys

    Add your Twilio API Key and Auth Token in the code, typically in a .env file or directly in the Python code.

6. Set Up Ngrok

    Go to Ngrok and sign up for an account.
    Get your auth token from your Ngrok dashboard.
    Run the following command in your terminal to authenticate Ngrok with your auth token:

    bash

    **ngrok authtoken YOUR_AUTHTOKEN**

7. Run the Application

    Start your Python application by running:

    bash

    **python app.py**

8. Expose the Application Using Ngrok

    Open a new terminal and run the following command to expose your local application:

    bash

    **ngrok http YOUR_PORT_NUMBER**

    Replace YOUR_PORT_NUMBER with the port number your application is running on (usually 5000).

