from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return f"Hello, {current_user.username}! This is your dashboard."