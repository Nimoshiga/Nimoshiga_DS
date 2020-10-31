from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':
        BHK_NO = request.form["BHK_NO"]
        BHK_NO = int(BHK_NO)
        SQUARE_FT = request.form["SQUARE_FT"]
        SQUARE_FT = int(SQUARE_FT)
        price = model.predict([[BHK_NO,SQUARE_FT]])
        
        return render_template('index.html', prediction_text="Price = {}".format(price))

if __name__ == "__main__":
    app.run()