import os
import io
from flask import Flask, render_template, request, redirect


# Initialise Flask
app = Flask(__name__)

def getData(request):
    req = request.form
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
    data = [int(gender), int(age), int(education), int(smoke), int(num_smoke), int(bpm), int(stroke), int(hyp), int(diab), float(totChol), float(sysBP), float(diaBP), float(bmi), float(hr), float(gluc)]
    return(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        data = getData(request)
        print(data)
        return redirect(request.url)

    return render_template("predict.html")
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
