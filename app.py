from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to App 1!"

@app.route('/contact-app2')
def contact_app2():
    response = requests.get('http://app2:5000/')
    return f"App 1 contacted App 2. App 2 says: {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)