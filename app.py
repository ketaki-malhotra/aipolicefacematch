#Ketaki's app.py

from io import BytesIO
from PIL import Image
import base64
import cv2


import urllib
import numpy as np
from datetime import timedelta
from urllib import response
from flask import Flask, render_template, redirect, url_for, session
from flask import request, Response
from flask import make_response, send_file
from time import sleep
import os
import json
import utils
#from logincofig import *



app = Flask(__name__,static_folder='static')
statusLogin = True
envStatus = True

'''
@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubdomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['Cache-Control'] = 'no-store'
    response.headers['Server'] = ''
    response.headers['Content-Security-Policy'] = "default-src 'self' 'unsafe-eval' 'unsafe-inline' *.accenture.com; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' *.accenture.com data:; connect-src 'self' *.accenture.com; font-src 'self' *.accenture.com; report-uri *.accenture.com/csp_report; form-action 'self';"
    return response
'''

@app.route("/")
def index():
    statusLogin = checkLoginStatus()
    if statusLogin == True :
        response = "Welcome to AI face match API for AI police"
        #response = make_response(render_template('base.html'))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubdomains'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Server'] = ''
        response.headers['Content-Security-Policy'] = "default-src 'self' 'unsafe-eval' 'unsafe-inline' *.accenture.com; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' *.accenture.com data:; connect-src 'self' *.accenture.com; font-src 'self' *.accenture.com; report-uri *.accenture.com/csp_report; form-action 'self';"
        return response
    else :
        response = make_response(Response())
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubdomains'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Server'] = ''
        response.headers['Content-Security-Policy'] = "default-src 'self' 'unsafe-eval' 'unsafe-inline' *.accenture.com; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' *.accenture.com data:; connect-src 'self' *.accenture.com; font-src 'self' *.accenture.com; report-uri *.accenture.com/csp_report; form-action 'self';"
        return response




@app.route('/face-match/', methods=[ "POST"])
def user_query_response():
    #statusLogin = checkLoginStatus()
    if statusLogin == True:
        filestr = request.files["img"].read()
        #convert string data to numpy array
        file_bytes = np.fromstring(filestr, np.uint8)
        # convert numpy array to image
        img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

        #f = image.read()
        #b = bytearray(f)
        #b = np.frombuffer(f)

        #print(type(image))
        #print(type(f))
        #print(type(b))

        #decoded = base64.b64decode(image)
        
        #b = np.array(Image.open(BytesIO(decoded)))

        


        
        #face_blob = utils.extract_face(img)[0]
        face_blob = img
        utils.fetch_imgs_from_azure_blob()
        criminal_faces_filenames= os.listdir("criminal_images")

        for criminal_face_filename in criminal_faces_filenames:
            criminal_face= cv2.imread("criminal_images/"+ criminal_face_filename)
            response = utils.compare(face_blob, criminal_face)
            if response == [True]:
                response_dict = { "response" : True, "criminal_name": criminal_face_filename}
                return json.dumps(response_dict)

        response_dict = { "response" : False, "criminal_name": None}
        return json.dumps(response_dict)

    else :
        response = make_response(redirect(redirectURL))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubdomains'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Server'] = ''
        response.headers['Content-Security-Policy'] = "default-src 'self' 'unsafe-eval' 'unsafe-inline' *.accenture.com; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' *.accenture.com data:; connect-src 'self' *.accenture.com; font-src 'self' *.accenture.com; report-uri *.accenture.com/csp_report; form-action 'self';"
        return response

@app.route('/healthy', methods=["GET", "POST"])
def healthcheck():
    return {"status": "healthy"}

if __name__ == '__main__':

    app.run( debug=True) 