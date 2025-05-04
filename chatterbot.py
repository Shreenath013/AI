from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Step A: Create chatbot instance
chatbot = ChatBot('SupportBot')

# Step B: Train with corpus data
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.english')

# Step C: Train with custom FAQ list for customer support
faq = [
    "Hi",
    "Hello! Welcome to Customer Support.",
    "What services do you offer?",
    "We offer product support, order tracking, and return assistance.",
    "How can I track my order?",
    "You can track your order using the tracking number sent to your email.",
    "What is your return policy?",
    "We accept returns within 30 days of delivery.",
    "Can I speak to a human?",
    "Our support staff is available from 9 AM to 5 PM, Monday to Friday.",
    "Thank you",
    "You're welcome!",
    "Bye",
    "Have a great day!"
]

list_trainer = ListTrainer(chatbot)
list_trainer.train(faq)

# Step D: User interaction
print("🤖 SupportBot: Hello! I'm your virtual assistant. Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "stop", "bye"]:
        print("🤖 SupportBot: Thank you for chatting with us. Goodbye!")
        break

    response = chatbot.get_response(user_input)
    print("🤖 SupportBot:", response)
