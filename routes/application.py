#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : api.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 24/06/2026
Licence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/links", methods=["GET"])
def links():
    return render_template("links.html")