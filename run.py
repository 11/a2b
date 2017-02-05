from flask import Flask, render_template, request
from twilio import twiml

import requests
import re


google_key = 'AIzaSyBEEF4_Wm3qivkCHiQpkEud7oPp7-FwrI0' 

app = Flask(__name__)

@app.route("/")
def run():
    return render_template("index.html")

@app.route("/sms", methods=["POST"])
def text():
    
    phone_num = request.form['From']
    message_body = request.form['Body']

    mesg_list = message_body.splitlines()
     
    origin=mesg_list[0].replace(" ","+")
    destination=mesg_list[1].replace(" ","+")
    
    google_url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+origin+',+NY&destination='+destination+',+NY&key='+google_key+'' 


    actual_dirs=""

    directions_json = requests.get(google_url).json()
    for i in directions_json['routes'][0]['legs'][0]['steps']:
        actual_dirs+=(i['html_instructions']).replace("<b>", "").replace("</b>","")+"\n"
        

    resp = twiml.Response()
    resp.message(actual_dirs)
    return str(resp)



if __name__ == "__main__":
    app.run("localhost", port=8080)
