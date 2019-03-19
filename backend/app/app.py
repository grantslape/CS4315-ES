from flask import Flask, jsonify
from datetime import datetime


app = Flask(__name__)

@app.route("/heartbeat")
def heartbeat():
    return jsonify(time=str(datetime.now()), env='local')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
