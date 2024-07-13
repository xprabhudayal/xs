# xs.py

from flask import Flask, request, jsonify
from pyngrok import ngrok
import threading

app = Flask(__name__)
generate_func = None
ngrok_api_token = None
port = None

def configure(generate_text_func, api_token, port_number):
    global generate_func, ngrok_api_token, port
    generate_func = generate_text_func
    ngrok_api_token = api_token
    port = port_number

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', '')
    response = generate_func(prompt)
    return jsonify(response)

def run_server():
    app.run(host='0.0.0.0', port=port)

def connect():
    ngrok.set_auth_token(ngrok_api_token)
    public_url = ngrok.connect(port=port)
    print(f'API Endpoint: {public_url}')
    
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
