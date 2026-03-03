from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load Model
model = pickle.load(open("model/disease_model.pkl", "rb"))

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    total = 100
    disease = 40
    healthy = 60

    return render_template(
        'dashboard.html',
        total=total,
        disease=disease,
        healthy=healthy
    )

@app.route('/result', methods=['POST'])
def result():
    try:
        budapest = float(request.form['budapest'])
        pest = float(request.form['pest'])
        fejer = float(request.form['fejer'])
        komarom = float(request.form['komarom'])
        veszprem = float(request.form['veszprem'])
        gyor = float(request.form['gyor'])

        features = np.array([[ 
            budapest, 0, 0, 0, 0, 0,
            fejer,
            gyor,
            0, 0, 0,
            komarom,
            0,
            pest,
            0, 0, 0, 0,
            veszprem,
            0
        ]])

        prediction = model.predict(features)[0]

        if prediction == 1:
            output = "High Chickenpox Risk"
        else:
            output = "Low Chickenpox Risk"

        return render_template("result.html", prediction=output)

    except Exception as e:
        return render_template("result.html", prediction="Error in Input Data")

# Important for Deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)