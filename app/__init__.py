from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder="./template", static_folder="./static")
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
