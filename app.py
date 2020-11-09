import asyncio
import random
import time

from flask import Flask, jsonify, request, json

app = Flask(__name__)


@app.route("/new", methods=['GET'])
def new():
    #data = request.json
    number = random.randint(1,100) / 100
    print(number)
    time.sleep(number)
    payload = {"message": f"call took {number} seconds"}
    return jsonify(payload)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001, debug = True)