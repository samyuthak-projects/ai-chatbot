import tkinter as tk
import random
from responses import intents

# function to generate bot reply
def get_response(user_input):

    user_input = user_input.lower()

    for intent in intents.values():
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I don't understand that yet."


# function triggered when user sends message
def send_message():

    user_message = entry.get()

    if user_message.strip() == "":
        return

    chat_window.insert(tk.END, "You: " + user_message + "\n")

    bot_reply = get_response(user_message)

    chat_window.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    entry.delete(0, tk.END)


# create window
window = tk.Tk()
window.title("SamBot Chatbot")

chat_window = tk.Text(window, height=20, width=50)
chat_window.pack()

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

window.mainloop()