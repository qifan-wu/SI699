from flask import Flask, request
import datetime
from predict import predict_label

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)

OutputInfo = {
    "name": "geek",
    "age": "22",
    "date": x,
    "programming": "python",
    "url":""
}

# Route for seeing a data
@app.route("/data")
def get_time():
    # Returning an api for showing in  reactjs
    # test_label = predict_label('https://github.com/Dong34/SI699/edit/main/backend/app.py')
    return {
        "Name": OutputInfo["name"], 
        "Age": OutputInfo["age"],
        "Date": OutputInfo["date"], 
        "programming": OutputInfo["programming"],
        "url": OutputInfo["url"],
        }

# Route for receiving input from user
@app.route("/acceptInput", methods=['POST'])
def get_urls():
    #Try this code
    #url = request.form.get("url")
    OutputInfo["url"] = "https://github.com/Dong34/SI699/blob/main/backend/predict.py"

# Running app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
