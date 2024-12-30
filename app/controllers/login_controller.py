# app/controllers/login_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.security.validate_teammate import checking_user


login_controller = Blueprint('login_controller', __name__)


@login_controller.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_teammate, teammate_data = checking_user(username, password)
        if is_teammate:
            if teammate_data is not None and teammate_data.active:
                login_user(teammate_data)
                if teammate_data.is_superuser:
                    return redirect(url_for('teammate_controller.list_users'))
                return render_template("user.html")
        flash('Invalid username or password')
        return redirect(url_for('login_controller.login'))
    return render_template('login.html')


@login_controller.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_controller.login'))
