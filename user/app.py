import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = "EVA"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)