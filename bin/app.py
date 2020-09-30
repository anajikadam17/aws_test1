# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:52:13 2020

@author: Anaji
"""
import flask
from flask import Flask, request
from summarizer import SummarizeDoc

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary

if __name__ == "__main__":
    app.run(host = 'localhost', port = 8080)