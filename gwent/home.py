from flask import Blueprint, render_template, request

app = Blueprint("static", __name__, template_folder="../templates")

@app.route("/")
def home():
    return render_template("home.html")