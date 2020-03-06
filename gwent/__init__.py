#!/usr/bin/python3
from flask import Flask, jsonify, request, send_from_directory

import gwent.home

app = Flask(__name__)
app.register_blueprint(gwent.home.app)

@app.errorhandler(404)
def try_static(e):
    print(request.path)
    return send_from_directory("../static", request.path[1:])
