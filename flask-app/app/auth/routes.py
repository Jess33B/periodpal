from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegistrationForm, ResetPasswordForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Logic for user login
        flash('Login successful!', 'success')
        return redirect(url_for('main.home'))
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Logic for user registration
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Logic for password reset
        flash('Password reset instructions have been sent to your email.', 'info')
        return redirect(url_for('auth.login'))
    return render_template('reset_password.html', form=form)