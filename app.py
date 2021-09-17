# Imports
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import torch
from classifier import Classifier
from preprocessor import Preprocessor
from transformers import BertTokenizerFast

#import torch.nn as nn
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import classification_report
#from transformers import AutoModel, BertTokenizerFast

# Settings
app = Flask(__name__)
model = None
#device = torch.device("cuda") # Setup GPU

# Load Data
"""
Load_dataset
Params Path -> current directory which contains the csv file
"""


""" Load saved model """
model = Classifier()
model.load_state_dict(torch.load('./data/saved_weights_final.pt', map_location=torch.device('cpu')))

tokenizer = Preprocessor()

# APP routes
@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        new_request = request.form
        if (new_request):
            text = []
            y = new_request['input_text']
            text.append(y)
            tokenize_input = tokenizer.tokenize_data(text)
            test_seq, test_mask = tokenizer.create_tensors(tokenize_input)
            pred = model(test_seq, test_mask)
            pred = pred.detach().numpy()
            pred = np.argmax(pred, axis = 1)
            pred = "Falsa" if pred == 0 else "Verdadera"
            return render_template("home.html", prediction="La noticia es {}".format(pred))

    return render_template("home.html")

# Entry point
if __name__ == '__main__':
    app.run()