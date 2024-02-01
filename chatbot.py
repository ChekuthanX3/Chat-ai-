from ChatterBot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('SimpleBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Define a function to interact with the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

if name == "main":
    print("SimpleBot: Hello! I'm your SimpleBot. Ask me anything.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("SimpleBot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"SimpleBot: {response}")
import subprocess
import sys

# Create and activate a virtual environment
subprocess.run([sys.executable, '-m', 'venv', 'venv'])
subprocess.run(['venv/bin/pip', 'install', '--upgrade', 'pip'])
subprocess.run(['venv/bin/pip', 'install', '-r', 'requirements.txt'])

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

