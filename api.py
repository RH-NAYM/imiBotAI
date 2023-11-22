from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json
import torch
import random
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from main import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()
bot_name = "ChatBot"

app = FastAPI()

class Item(BaseModel):
    text: str



@app.post("/chatbot")
async def process_item(item: Item):
    try:
        sentence = item.text
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.8:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    bot = {"You": item.text, bot_name:random.choice(intent['responses'])}
        else:
            bot = {"You":item.text,bot_name:"Invalid Query"}

        result = calculate(bot)
        chatbot = {bot_name:result}
        return chatbot

    finally:
        torch.cuda.empty_cache()
        pass

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="127.0.0.1", port=8000)
    finally:
        torch.cuda.empty_cache()
