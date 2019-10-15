import os
import re
import json
import pprint

#Linux
#os.system("ls")
#windows
#os.system("dir")
app_name=""

def cmd(cmd):
    if cmd.find("cd ") > -1:
        path = cmd[cmd.find("cd ")+3:]
        cmd_cd(path)
    elif cmd.find("chdir ") > -1:
        path = cmd[cmd.find("chdir ")+6:]
        cmd_cd(path)
    elif cmd.find("cwd") > -1:
        cmd_cwd()
    elif re.fullmatch(cmd,"ls") != None:
        cmd_ls()
    elif re.fullmatch(cmd,"dir") != None:
        cmd_ls()
    else:
        os.system(cmd)

def cmd_cd(path):
    os.chdir(path)

def cmd_cwd():
    path=os.getcwd()
    print(path)

def cmd_ls():
    path = os.getcwd()
    fl = os.listdir(path)
    print(fl)

def show_j(data):
    pprint.pprint(data, width=40)

def creator_app():
    print("Please input create application name")
    app_name = input()
    cmd("mkdir create_app")
    cmd("chdir create_app")
    cmd("mkdir " + app_name + "_dev")
    cmd("chdir " + app_name + "_dev")
    cmd("mkdir " + app_name)
    cmd("chdir " + app_name)
    cmd("npm init -y")
    cmd("npm install electron --save-dev")
    cmd("npm install --save request")
    cmd("npm install --save request-promise")
    cmd("ls")
    with open('package.json') as f:
        pack_d = json.load(f)
    pack_d["author"] = "udagawa tomohiro"
    pack_d["scripts"]["start"] = "electron index.js"
    show_j(pack_d)
    with open('package.json','w') as f:
        json.dump(pack_d,f,indent=4)

    with open('hello.py','w') as f:
        f.write("#!/usr/bin/env python\n")
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("from __future__ import print_function\n")
        f.write("import time\n")
        f.write("from flask import Flask\n")
        f.write("\n")
        f.write("app = Flask(__name__)\n")
        f.write("\n")
        f.write('@app.route("/")\n')
        f.write("\n")
        f.write("def hello():\n")
        f.write("    return 'Hello World!<br>This is powered by Python backend.'\n")
        f.write("\n")
        f.write('if __name__ == "__main__":\n')
        f.write("    print('on hello')\n")
        f.write("    app.run(host='127.0.0.1', port=5000)\n")

    with open('index.js','w') as f:
        f.write("'use strict';\n")
        f.write("const electron = require('electron');\n")
        f.write("const app = electron.app;\n")
        f.write("const BrowserWindow = electron.BrowserWindow;\n")

        f.write("let mainWindow;\n")

        f.write("app.on('ready', function() {\n")
        f.write("// create window\n")
        f.write("  mainWindow = new BrowserWindow({width: 600, height: 400});\n")
        f.write("  mainWindow.loadURL('file://' + __dirname + '/index.html');\n")
        f.write("  mainWindow.webContents.openDevTools();\n")
        f.write("  mainWindow.on('closed', function() {\n")
        f.write("    mainWindow = null;\n")
        f.write("  });\n")
        f.write("});\n")

    cmd("npm start")

if __name__ == "__main__":
    creator_app()




