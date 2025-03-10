#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza
#______________________________________________________________________________________________________________________

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import subprocess

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Flag oculta
FLAG = "CTF{SSRF_And_Command_Injection_Fun}"

# Usuario y contraseña para autenticación
USER_CREDENTIALS = {
    "admin": "admin"
}

# Recurso interno (simulado)
INTERNAL_RESOURCE = {
    "flag": FLAG
}

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USER_CREDENTIALS.get(username) == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/api/fetch', methods=['GET'])
def fetch_resource():
    if 'username' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    # Vulnerabilidad de SSRF
    try:
        response = requests.get(url)
        return response.json()
    except:
        return jsonify({"error": "Failed to fetch resource"}), 500

@app.route('/api/execute', methods=['POST'])
def execute_command():
    if 'username' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    command = request.json.get('command')
    if not command:
        return jsonify({"error": "Command parameter is required"}), 400

    # Vulnerabilidad de Inyección de Comandos
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return jsonify({"result": result})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)