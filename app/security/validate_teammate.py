import re
from app.security.encryption import encrypt_password
from app.models.teammate_model import teammates


def prepare_new_user_data(teammate_instance):
    if not validate_new_user_data(teammate_instance.username, 'username', teammate_instance.id):
        return False, "Invalid username"
    if not validate_new_user_data(teammate_instance.name, 'name'):
        return False, "Invalid name"
    if not validate_new_user_data(teammate_instance.password, 'password'):
        return False, "Invalid password"
    if not validate_new_user_data(teammate_instance.email, 'email'):
        return False, "Invalid email"
    teammate_instance.password = encrypt_password(teammate_instance.password)

    # Return a new teammate object
    return True, teammate_instance


def validate_new_user_data(data, data_type, current_user_id=None):
    if data_type == 'username':
        if validate_username(data, current_user_id):
            return True
    elif data_type == 'password':
        if validate_password(data):
            return True
    elif data_type == 'name':
        if validate_name(data):
            return True
    elif data_type == 'email':
        if validate_email(data):
            return True
    return False


def validate_name(name):
    if re.match(r'^[a-zA-Z]{6,60}$', name):
        return True
    return False


def validate_email(email):
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return True
    return False


def validate_password(password):
    if re.match(r'^[a-zA-Z0-9_]{6,20}$', password):
        return True
    return False


def validate_username(username, current_user_id=None):
    existing_user = teammates.query.filter_by(username=username).first()
    if existing_user is None or existing_user.id == current_user_id:
        if re.match(r'^[a-zA-Z0-9_]{6,20}$', username):
            return True
    return False


def check_password(password):
    encrypted_input_password = encrypt_password(password)
    user = teammates.query.filter_by(password=encrypted_input_password).first()
    if user:
        return True
    return False


def checking_user(username, password):
    encrypted_input_password = encrypt_password(password)
    user = teammates.query.filter_by(username=username, password=encrypted_input_password).first()
    if user:
        return True, user
    return False, None
