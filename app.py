from flask import Flask, send_file, request, jsonify, render_template, Response
import uuid
from module.poe import *
from module.editor import *
import requests
import random
import psycopg2
app = Flask(__name__)


db_url = "postgres://koyeb-adm:scWmuEJ2oBL7@ep-fragrant-art-a2bppp1o.eu-central-1.pg.koyeb.app/postgres"

# Membuat koneksi
try:
    conn = psycopg2.connect(db_url)
    # conn.autocommit = True  # Mengaktifkan mode autocommit
    print("Koneksi berhasil")
except Exception as e:
    print(f"Gagal terhubung ke database: {e}")
    exit()

# Membuat cursor
cur = conn.cursor()

# Menjalankan perintah CREATE DATABASE
try:
    cur.execute('GRANT ALL ON SCHEMA public TO koyeb-adm;')
    cur.execute("""
CREATE TABLE nama_tabel (
    id SERIAL PRIMARY KEY,
    kolom1 VARCHAR(100),
    kolom2 INTEGER,
    kolom3 DATE
);
""")
    print("Database berhasil dibuat")
except Exception as e:
    print(f"Kesalahan saat membuat database: {e}")

# Menutup cursor dan koneksi
cur.close()
conn.close()


exit()

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