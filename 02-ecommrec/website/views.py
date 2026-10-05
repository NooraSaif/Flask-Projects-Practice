from flask import Blueprint # A blueprint class is a way to organize routes, templates, and logic into smaller groups. is a way to split the app into logical sections:
# views for main pages
# auth for login/register
# admin for admin dashboard
# This keeps the app organized and easier to maintain.
views = Blueprint('views', __name__)

@views.route('/') # This decorator registers a URL route. When a user visits the root URL ("/"), the home() function will be executed.
def home():
    return "<h1>Home Page</h1>"