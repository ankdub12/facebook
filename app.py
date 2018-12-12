from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

@app.route("/webhooks/inbound-message", methods=['POST'])
def inbound_message():
    data = request.get_json()
    pprint(data)
    return "200"

if __name__ == '__main__':
    app.run(debug= "http://1545845d.ngrok.io", port= 3000)