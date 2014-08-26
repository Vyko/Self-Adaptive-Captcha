#!/usr/bin/python
import sys
import sqlite3 as lite
from flask import Flask, render_template, jsonify, request
from api.sac_controller import Controller

app = Flask(__name__)


## WEBSITE
@app.route('/')
def index():
    return render_template('index.html', title = 'Sefl-Adaptive CAPTCHA')

## API
@app.route('/api/generate', methods = ['POST'])
def generate():
    ctrl = Controller()
    return jsonify(ctrl.generateCaptcha(request.form))

@app.route('/api/identify/<num>')
def identify(num):
    ctrl = Controller()
    return jsonify(ctrl.getCaptchaType(num))

@app.route('/api/submit/<num>', methods = ['POST'])
def submit(num):
    ctrl = Controller()
    return jsonify(ctrl.verifyCaptcha(request.form, num))

if __name__ == '__main__':
    app.debug = True
    app.run()
