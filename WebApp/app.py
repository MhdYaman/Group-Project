import os
import io
import numpy as np
from flask import Flask, render_template, request, redirect
import googleapiclient.discovery
from google.api_core.client_options import ClientOptions


# Initialise Flask
app = Flask(__name__)

def getData(request):
    req = request.form
    gender = req['gender']
    age = req['age']
    num_smoke = req['num_smoke']
    stroke = req['stroke']
    sysBP = req['sysBP']
    gluc = req['gluc']
    data = [int(gender), int(age), int(num_smoke), int(stroke), float(sysBP), float(gluc)]
    return(data)

def predict_json(project, region, model, instances, version=None):
    """Send json data to a deployed model for prediction.

    Args:
        project (str): project where the Cloud ML Engine Model is deployed.
        region (str): regional endpoint to use; set to None for ml.googleapis.com
        model (str): model name.
        instances ([Mapping[str: Any]]): Keys should be the names of Tensors
            your deployed model expects as inputs. Values should be datatypes
            convertible to Tensors, or (potentially nested) lists of datatypes
            convertible to tensors.
        version: str, version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the
            model.
    """
    # Create the ML Engine service object.
    # To authenticate set the environment variable
    GOOGLE_APPLICATION_CREDENTIALS="key.json"
    prefix = "{}-ml".format(region) if region else "ml"
    api_endpoint = "https://{}.googleapis.com".format(prefix)
    client_options = ClientOptions(api_endpoint=api_endpoint)
    service = googleapiclient.discovery.build(
        'ml', 'v1', client_options=client_options)
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=["GET", "POST"])
def predict():
    response = ""
    if request.method == "POST":
        data = getData(request)
        print(data)
        reply = predict_json('heartdisease-297903','us-east1','Heart_Disease_New',[data])
        print(reply)
        reply = reply[0]
        if reply == 0:
            response = "It is unlikely that you will have heart disease in 10 years"
        elif reply == 1:
            response = "It is likely that you will have heart disease in 10 years"
    return render_template("predict.html", result=response)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
