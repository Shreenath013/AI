import re

# Predefined responses
responses = {
    r'hi|hello|hey': "Hello! How can I assist you today?",
    r'what.*your name': "I'm a customer service chatbot.",
    r'how.*you': "I'm just a bot, but I'm here to help!",
    r'what time.*open|hours': "Our store is open from 9 AM to 9 PM every day.",
    r'where.*located': "We are located at Katraj Khondwa road.",
    r'do you have (.*)': "Let me check. Could you specify the brand or model?",
    r'bye|goodbye': "Goodbye! Have a great day!",
}

# Function to match user input with responses
def chatbot_response(user_input):
    for pattern, response in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I didn't understand that. Can you rephrase?"

# Chatbot loop
print("Customer Support Bot: Hello! How can I help you today? (Type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Customer Support Bot: Thank you for chatting! Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Customer Support Bot: {response}")
