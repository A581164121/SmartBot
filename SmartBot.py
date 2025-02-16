from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Step 1: Create ChatBot instance
chatbot = ChatBot(
    "SmartBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///db.sqlite3",
    read_only=False,  # Allow learning
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ]
)

# Step 2: Train with built-in English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Step 3: Train with custom YAML file
trainer.train("./custom_train.yml")

# Step 4: Start chatting after training
print("\nSmartBot is ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("SmartBot:", response)
import os

trainer = ChatterBotCorpusTrainer(chatbot)

# Get the absolute path of your YAML file
current_directory = os.path.dirname(os.path.abspath(__file__))
custom_yaml_path = os.path.join(current_directory, "custom_train.yml")

trainer.train("chatterbot.corpus.english")
trainer.train(custom_yaml_path)  # Use absolute path
