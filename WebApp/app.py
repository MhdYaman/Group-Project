import os
import io
from flask import Flask, render_template, request, redirect
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
    if request.method == "POST":
        req = request.form
        print(req)
        gender = req['gender']
        age = req['age']
        education = req['edu']
        smoke = req['smoke']
        num_smoke = req['num_smoke']
        if smoke == "no":
            num_smoke = 0
        bpm = req['bpm']
        stroke = req['stroke']
        hyp = req['hyp']
        diab = req['diab']
        totChol = req['TotChol']
        sysBP = req['sysBP']
        diaBP = req['diaBP']
        bmi = req['bmi']
        hr = req['hr']
        gluc = req['gluc']
        print(gender, age, education, smoke, num_smoke, bpm, stroke, hyp, diab, totChol, sysBP, diaBP, bmi, hr, gluc)
        return redirect(request.url)

    return render_template("predict.html")
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
