#flask twilio libraries
from flask import Flask, render_template, request
from twilio import twiml

#built in python libraries
import requests
import re

#google API KEY
google_key = 'AIzaSyBEEF4_Wm3qivkCHiQpkEud7oPp7-FwrI0' 

#create an instance of Flask Server 
app = Flask(__name__)

#webhook for route directory
@app.route("/")
def run():
    return render_template("index.html")

#webhook for an sms text
@app.route("/sms", methods=["POST"])
def text():    
    #store the phone numbner and message body
    phone_num = request.form['From']
    message_body = request.form['Body']

    #split the msg into a list based on the '\n' char
    mesg_list = message_body.splitlines()
    
    #first line is hardcoded for the place the usr is currently at
    #google maps api forces for there to be a + inbetween each space
    origin=mesg_list[0].replace(" ","+")
    
    #second line is hardcoded for the place the usr destination
    #google maps api forces for there to be a + inbetween each space
    destination=mesg_list[1].replace(" ","+")
    
    #google api url
    google_url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+origin+',+NY&destination='+destination+',+NY&key='+google_key+'' 

    #empty string that will be the actual directions
    actual_dirs=""
    
    #request for the directions from google maps
    directions_json = requests.get(google_url).json()
    count=1
    
    #janky way to loop through json data
    for i in directions_json['routes'][0]['legs'][0]['steps']:
        actual_dirs.join((str(count)+".)  "+i['html_instructions']).replace("<b>", "").replace("</b>","")+"\n\n")
        count+=1

    #create an instance of a SMS response and text back the directions
    resp = twiml.Response() 
    resp.message(actual_dirs)
    
    return str(resp)


#run server
if __name__ == "__main__":
    app.run("localhost", port=8080)
