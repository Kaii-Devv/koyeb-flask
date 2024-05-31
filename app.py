from flask import Flask, send_file, request, jsonify, render_template, Response
import uuid
from module.poe import *
from module.editor import *
import requests
import random
import psycopg2
app = Flask(__name__)

#
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
    if prompt:
        login(''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(20)])+'@vjuum.com')

if __name__ == "__main__":
    app.run()