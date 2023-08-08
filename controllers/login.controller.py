from flask import jsonify
import app

@app.route('/login', methods=['POST'])
def createUser():
