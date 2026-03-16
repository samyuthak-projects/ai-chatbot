import random
from responses import intents

print("Chatbot started! Type 'quit' to exit.")

while True:

    user_input = input("You: ").lower()

    if user_input == "quit":
        print("Bot: Goodbye!")
        break

    response_found = False

    for intent in intents.values():

        for pattern in intent["patterns"]:

            if pattern in user_input:

                reply = random.choice(intent["responses"])
                print("Bot:", reply)

                response_found = True
                break

        if response_found:
            break

    if not response_found:
        print("Bot: Sorry, I don't understand that yet.")