from flask import Flask, request, jsonify, session
import datetime
from predict_label import predict_label

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
app.secret_key = 'si699'

test = {
    "name": "geek",
    "age": "22",
    "date": x,
    "programming": "python",
}

# Route for seeing a data
@app.route("/data")
def get_time():
    url = session.get("url")
    label = str(predict_label(url))
    return {
        "Name": test["name"], 
        "Age": test["age"],
        "Date": test["date"], 
        "programming": test["programming"],
        "url": url,
        "label": label,
    }

# Route for receiving input from user
@app.route("/submit-form", methods=['POST'])
def get_urls():
    data = request.get_json()
    url = data["url"]
    session["url"] = url
    return jsonify({'url': url})

# Running app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
