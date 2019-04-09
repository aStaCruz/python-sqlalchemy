from flask import Flask, render_template, request, redirect, Response, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime
from config import Config as cfg
import requests
import json
import os, sys
import redis
import math
import ast 

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lbyrzkwzicgxus:d75a210613d87099573252580e5f3523ffcd5dd1722751815ea0e8db9268a800@ec2-23-23-173-30.compute-1.amazonaws.com:5432/d672b3e2ginsol'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import FeatureRequest

#create
@app.route('/send_request', methods=['POST'])
def send_request():
    #try:
    title = request.form['title']
    description = request.form['description']
    client = request.form['client']
    clientPriority = request.form['clientPriority']
    targetDate = request.form['targetDate']
    productArea = request.form['productArea']

    #debug kek
    print("title: {0}".format(title))
    print("description: {0}".format(description))
    print("client: {0}".format(client))
    print("clientPriority: {0}".format(clientPriority))
    print("targetDate: {0}".format(targetDate))
    print("productArea: {0}".format(productArea))

    reg = FeatureRequest(title, description, client, clientPriority, targetDate, productArea)
    db.session.add(reg)
    db.session.commit()

    return json.dumps({ "response": ('added') }), 200, {'ContentType':'application/json'}
    """except: 
        print("An exception occurred")
        return json.dumps({ "response": ('An exception occurred') }), 503, {'ContentType':'application/json'}"""

#retrieve
@app.route('/requests', methods=['GET'])
def requests():
    FR = FeatureRequest.query.all()
    return (render_template('requests.html', requests=FR))

#update
@app.route('/update', methods=['POST'])
def update():
    rowID = request.form['row-id']
    title = request.form['title']
    description = request.form['description']
    client = request.form['client']
    clientPriority = request.form['clientPriority']
    targetDate = request.form['targetDate']
    productArea = request.form['productArea']

    FR = FeatureRequest.query.filter_by(id=rowID).first()

    FR.title = title
    FR.description = description
    FR.client = client
    FR.clientPriority = clientPriority
    FR.targetDate = targetDate
    FR.productArea = productArea

    db.session.commit()

    return json.dumps({ "response": ('updated') }), 201, {'ContentType':'application/json'}

#delete
@app.route('/delete', methods=['POST'])
def delete():
    rowID = request.form['row-id']

    FR = FeatureRequest.query.filter_by(id=rowID).first()

    db.session.delete(FR)
    db.session.commit()

    return json.dumps({ "response": ('deleted') }), 201, {'ContentType':'application/json'}

@app.route('/', methods=['GET'])
def index():
    return (render_template('index.html'))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
