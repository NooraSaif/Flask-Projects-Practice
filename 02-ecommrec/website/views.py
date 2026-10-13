from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/') # URL route. When a user visits the root URL ("/"), the home() function will be executed.
def home():
    return render_template("home.html")

