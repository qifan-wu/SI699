from flask import Flask, request, jsonify, session
import datetime
from predict_label import predict_label
import sys
import redis
import mysql.connector

x = datetime.datetime.now()

mydb = mysql.connector.connect(
    host = "localhost",
    user = "si699",
    password = "SI699_password",
    database="si699_db",
)
mycursor = mydb.cursor()

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
    newURL = session.get("newURL")

    app.logger.info(url)
    app.logger.info(newURL)

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
        "newURL": newURL,
        "label":str(label),
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

@app.route("/submit-newURL", methods=['POST'])
def getNewUrls():
    data = request.get_json()
    # print(data, file=sys.stderr)
    # print(data["newURL"], file=sys.stderr)
    newURL = data["newURL"]
    label = data["selectValue"]

    sql = 'INSERT INTO si699_userInput (url, label, date) VALUES (%s, %s, %s)'
    val = (newURL, label, x)
    mycursor.execute(sql, val)

    return jsonify({"message": "successfully inserted new url and label"})

# Route for submitting the predicted lable is wrong
# @app.route('/submit_error', methods=['POST'])
# def submit_error():
#     return 'Error submitted'

# Running app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

