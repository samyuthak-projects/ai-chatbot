from responses import responses

print("Chatbot started! Type 'quit' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "quit":
        print("Bot: Goodbye!")
        break

    reply = responses.get(user_input, "Sorry, I don't understand that.")

    print("Bot:", reply)