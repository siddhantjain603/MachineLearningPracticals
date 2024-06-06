import pickle
from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

## import ridge regresor model and standard scaler pickle
regression_model=pickle.load(open('models/lassoCV.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        MedInc=float(request.form.get('MedInc'))
        HouseAge=float(request.form.get('MedInc'))
        AveRooms=float(request.form.get('MedInc'))
        AveBedrms=float(request.form.get('MedInc'))
        Population=float(request.form.get('MedInc'))
        AveOccup=float(request.form.get('MedInc'))
        Latitude=float(request.form.get('MedInc'))
        Longitude=float(request.form.get('MedInc'))

        new_data_scaled=standard_scaler.transform([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
        result=regression_model.predict(new_data_scaled)

        return render_template('home.html',result=result[0])

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
