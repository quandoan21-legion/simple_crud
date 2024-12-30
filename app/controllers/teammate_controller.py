from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from openpyxl.styles.builtins import total

from app.models.teammate_model import teammates
from app.security.encryption import encrypt_password
from app.security.validate_teammate import check_password

teammate_controller = Blueprint('teammate_controller', __name__)
limit = 10


@teammate_controller.route('/teammates')
@login_required
def list_users(current_page=1):
    users = teammates.query.limit(limit).all()
    return render_template('teammates.html', users=users, total_pages=round(count_all_users() / limit),
                           current_page=current_page)


@teammate_controller.route('/disable-account/<int:id>', methods=['POST'])
@login_required
def disable_account(id):
    from app import db
    user = teammates.query.get(id)
    user.active = False
    db.session.commit()
    return redirect(url_for('login_controller.logout'))


@teammate_controller.route('/change-password/<int:id>', methods=['GET', 'POST'])
@login_required
def change_password(id):
    from app import db
    user = teammates.query.get(id)
    if request.method == 'POST':
        if request.form['new_password'] != request.form['confirm_password']:
            flash("The new Password and Confirm Password fields must match")
            return render_template("change-password.html", user=user)
        if check_password(request.form['old_password']):
            user.password = encrypt_password(request.form['new_password'])
            db.session.commit()
            flash("Password changed successfully")
            return render_template("user.html")
        else:
            flash("Old password is incorrect")
            return render_template("change-password.html", user=user)
    elif request.method == 'GET':
        return render_template("change-password.html", user=user)


@teammate_controller.route('/search-user', methods=['GET'])
@login_required
def search_user(offset=0):
    offset = int(request.args.get('offset', 0))
    search_term = request.args.get('search', default='')
    current_page = offset // limit + 1  # Assuming 10 items per page
    total_pages = (teammates.query.count() + 9) // limit
    search_results = teammates.query.filter(
        teammates.username.ilike(f'%{search_term}%') |
        teammates.name.ilike(f'%{search_term}%') |
        teammates.email.ilike(f'%{search_term}%')
    ).limit(limit).offset(offset * limit).all()
    return render_template('teammates.html', users=search_results, search_term=search_term, current_page=current_page,
                           total_pages=total_pages)


def count_all_users():
    return teammates.query.count()
