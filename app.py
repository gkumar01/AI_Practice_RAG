#! /usr/bin/python3
""" Flask implementation """

import os

from flask import Flask, jsonify, render_template, request
from pytrie import StringTrie

app = Flask(__name__, static_folder="", template_folder="templates/")

@app.route("/")
def index():
    return render_template('base.html',
                           title="RAG System",
                           description="Flask & Jinja2"
                           )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)