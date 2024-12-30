from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from app import db
from app.models.teammate_model import teammates

teammate_info_controller = Blueprint('teammate_info_controller', __name__)


@teammate_info_controller.route('/teammate-info/<int:id>', methods=['GET', 'POST'])
@login_required
def teammate_info(id):
    user = teammates.query.get(id)
    if request.method == 'POST':
        user.active = request.form['active'] == "True"
        db.session.commit()
        return redirect(url_for('teammate_controller.list_users'))
    return render_template('teammate-info.html', user=user)


def populate_teammate_info(teammate_info, form):
    teammate = teammates()
    teammate.id = teammate_info.id
    teammate.username = teammate_info.username
    teammate.email = form.get('email')
    teammate.name = form.get('name')
    teammate.password = form.get('password')
    teammate.active = form.get('active') == "True"
    return teammate
