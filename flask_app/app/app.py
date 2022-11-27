import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello_index():
    return render_template("index.html")
@app.route("/predict",methods=["POST"])
def predict():
    age=int(request.form.get('age'))
    print(age)
    job=int(request.form.get('job'))
    print(job)
    marital=int(request.form.get('marital'))
    print(marital)
    education=int(request.form.get('education'))
    print('education')
    previous_campaign_outcome=request.form.get('previous_campaign_outcome')
    print(previous_campaign_outcome)
    model_data=[age,job,marital,education,previous_campaign_outcome]
    data=np.array(model_data).reshape(1,-1)
    Model_choice=request.form.get('Model_Choice')
    if Model_choice=='neural_reg2':
        selection= 'Neural Networks'
        neural_reg2=pickle.load(open('neural_networks_model.pkl','rb'))
        prediction=neural_reg2.predict(data)
    return render_template('index.html',age=age,education=education, job=job, prediction=prediction)
    return redirect(url_for("index"))
