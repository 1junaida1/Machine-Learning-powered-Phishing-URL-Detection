#importing required libraries
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
from mail import sendmail
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

file = open("pickle\modelnew.pkl","rb")
gbc = pickle.load(file)
file.close()
app = Flask(__name__)

@app.route("/mail", methods=["POST"])
def mail():
    
    sub = request.form["sub"]
    email = request.form["email"]
    msg = request.form["message"]
    sendmail(email,msg,sub)
    print(sub,email,msg)
    return  render_template("index.html",success="Your message is sent successfully")
    

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/check", methods=["GET", "POST"])
def check():
    return render_template("project.html")
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        url = request.form["urlInput"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]
        #1 is safe       
        #-1 is unsafe
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        if(y_pred ==1 ):
            
            pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
            return render_template('safe.html' )
        # return render_template('index.html',xx =round(y_pro_non_phishing,2),url=url )
        else: 
        
            return render_template('warning.html' )

    return render_template("index.html", xx =-1)
def predict():
     url=request.values['url']
     print(url)
     data=FeatureExtraction(url)
     print(data)

if __name__ == "__main__":
    app.run(debug=True)
