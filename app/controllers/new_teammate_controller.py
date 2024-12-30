from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from app import db
from app.security.validate_teammate import prepare_new_user_data
from app.models.teammate_model import teammates

new_teammate_controller = Blueprint('new_teammate_controller', __name__)


@new_teammate_controller.route('/new-teammate', methods=['GET', 'POST'])
@login_required
def new_user():
    if request.method == 'POST':
        teammate_instance = populate_teammate_info(request.form)
        is_valid , data = prepare_new_user_data(teammate_instance)
        if is_valid:
            add_new_teammate(data)
            flash('New user added successfully')
            return redirect(url_for('teammate_controller.list_users')) # Redirect to the list of users
        else:
            flash(data)
            return redirect(url_for('new_teammate_controller.new_user'))
        return redirect(url_for('teammate_controller.list_users'))
    return render_template('new-teammates.html')

def populate_teammate_info(form):
    teammate = teammates()
    teammate.username = form.get('username')
    teammate.email = form.get('email')
    teammate.name = form.get('name')
    teammate.password = form.get('password')
    return teammate

def add_new_teammate(new_teammate):
    db.session.add(new_teammate)
    db.session.commit()


