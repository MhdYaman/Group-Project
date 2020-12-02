import os
import io
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from google.cloud import translate
from google.cloud import vision

# Initialise Flask
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/predict', methods=["GET", "POST"])
def predict():
    return render_template("predict.html")
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
