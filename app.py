from flask import Flask, send_file, request, jsonify, render_template, Response
import uuid
from module.poe import *
from module.editor import *
import requests
import random
from cryptography.fernet import Fernet
import json
import psycopg2
app = Flask(__name__)

#
def enc(text):
    de = str(text.encode())
    key = b'JWCoVduCIBjJdSj8Y8965uulbg60W3-twaY-xitc5_Q='
    f = Fernet(key)
    token = f.encrypt(strjs)
    return token

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'

@app.route('/api/image')
def image():
    prompt = request.args.get('prompt')
    if prompt:
        result = generateImagev2(prompt)
        return result

@app.route('/api/gpt4o')
def gpt():
    prompt = request.args.get('prompt')
    token = request.args.get()
    if prompt:
        if not token:
            token = login(''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(20)])+'@vjuum.com')
        key = b'JWCoVduCIBjJdSj8Y8965uulbg60W3-twaY-xitc5_Q='
        f = Fernet(key)
        cookies = f.decrypt(token)
        
        respon = sendMessage(prompt,cookies=cookies)
        return {'text':respon,'token':token}
        

if __name__ == "__main__":
    app.run()