#!/usr/bin/python
import sys
import sqlite3 as lite
from flask import Flask, render_template, jsonify, request
from api.sac_core import Core

app = Flask(__name__)



"""This is the file that manages the url request and instantiate the Core object to generate, identify or submit a CAPTCHA"""

## API
@app.route('/api/generate', methods = ['POST'])
def generate():
    core = Core()
    return jsonify(core.generateCaptcha(request.form))

@app.route('/api/identify/<num>')
def identify(num):
    core = Core()
    return jsonify(core.getCaptchaType(num))

@app.route('/api/submit/<num>', methods = ['POST'])
def submit(num):
    core = Core()
    return jsonify(core.verifyCaptcha(request.form, num))

if __name__ == '__main__':
    app.debug = True
    app.run()
