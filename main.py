def chatbot_response(message):
    message = message.strip().lower()

    if message in {"hello", "hi", "hey"}:
        return "Hi! How can I help you?"
    elif "how are you" in message:
        return "I'm fine, thanks! How are you?"
    elif "your name" in message:
        return "I'm a simple Python rule-based chatbot."
    elif "python" in message:
        return "Python is a popular programming language used for many types of applications."
    elif message in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that yet. Try saying hello, asking how I am, or saying bye."


def run_chatbot():
    print("\n=== CodeAlpha Basic Chatbot ===")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_message = input("You: ")
        response = chatbot_response(user_message)
        print("Bot:", response)

        if user_message.strip().lower() in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    run_chatbot()
