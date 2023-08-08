from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3050)