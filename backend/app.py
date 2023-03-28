from flask import Flask, request, jsonify, session
import datetime
from predict_label import predict_label
import sys
import redis

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
app.secret_key = 'si699'

pool = redis.ConnectionPool(host = '127.0.0.1', port = 6379, db = 0)
redisObj = redis.Redis(connection_pool = pool)

OutputInfo = {
    "name": "geek",
    "age": "22",
    "date": x,
    "programming": "python",
}

def readCache(key):
    return redisObj.get(key).decode()

def setCache(key, value):
    redisObj.set(key, value, ex = 600)

# Route for seeing a data
@app.route("/data")
def getLabel():
    url = session.get("url")
    app.logger.info(url)
    if redisObj.exists(url) == 1:
        label = readCache(url)
    else:
        label = predict_label(url)
        app.logger.info(label)
        setCache(url, str(label))
    return {
        "Name": OutputInfo["name"], 
        "Age": OutputInfo["age"],
        "Date": OutputInfo["date"], 
        "programming": OutputInfo["programming"],
        "url": url,
        "label":label,
        }

# Route for receiving input from user
@app.route("/submit-form", methods=['POST'])
def getUrls():
    data = request.get_json()
    print(data, file=sys.stderr)
    print(data["url"], file=sys.stderr)
    url = data["url"]
    session["url"] = url
    return jsonify({'url': url})

# Route for submitting the predicted lable is wrong
@app.route('/submit_error', methods=['POST'])
def submit_error():
    return 'Error submitted'

# Running app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

