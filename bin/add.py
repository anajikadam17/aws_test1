# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:16:35 2020

@author: Anaji
"""
import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "YAY!!! its working"


@app.route('/add',methods=['GET'])
def addNum():
    a = 2
    b = 3
    return "The sm of {} and {} is {}".format(a,b,a+b)

if __name__ == "__main__":
    app.run(host = 'localhost', port = 8080)