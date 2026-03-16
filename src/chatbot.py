import random
from responses import responses

print("Chatbot started! Type 'quit' to exit.")

while True:

    user_input = input("You: ").lower()

    if user_input == "quit":
        print("Bot: Goodbye!")
        break

    response_found = False

    for keyword in responses:
        if keyword in user_input:
            reply = random.choice(responses[keyword])
            print("Bot:", reply)
            response_found = True
            break

    if not response_found:
        print("Bot: Sorry, I don't understand that.")