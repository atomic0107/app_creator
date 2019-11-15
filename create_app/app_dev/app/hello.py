#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import time
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
   title = 'hello world'
   message = 'Hello World!<br>This is powered by Python backend.'
   return render_template('index.html',
                       message=message, title=title)

if __name__ == "__main__":
    app.debug = True # デバッグモード有効化
    print('on hello')
    app.run(host='127.0.0.1', port=5000)
