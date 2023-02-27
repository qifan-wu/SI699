from flask import Flask
import datetime
from predict import predict_label


x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)

# Route for seeing a data
@app.route('/data')
def get_time():
    # Returning an api for showing in  reactjs
    test_label = predict_label('https://github.com/Dong34/SI699/edit/main/backend/app.py')
    return {
        'Name':"geek", 
        "Age":"22",
        "Date":x, 
        "programming":"python",
        "test_label":test_label,
        }

# Running app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
