import sys
import os

import bcrypt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# tests/test_login_controller.py
import pytest
from flask import url_for
from app import create_app, db
from app.models.teammate_model import teammates as Teammate


@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_login_get(client):
    response = client.get(url_for('login_controller.login'))
    assert response.status_code == 200
    assert b'Login' in response.data


def test_login_post_valid(client):
    # Hash the password before adding the test user to the database
    hashed_password = bcrypt.hashpw('password123'.encode('utf-8'), bcrypt.gensalt())
    test_user = Teammate(username='testuser', password=hashed_password, active=True, is_superuser=False)
    db.session.add(test_user)
    db.session.commit()

    response = client.post(url_for('login_controller.login'), data={
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 302  # Redirect after successful login


def test_login_post_invalid(client):
    response = client.post(url_for('login_controller.login'), data={
        'username': 'invaliduser',
        'password': 'wrongpassword'
    })
    assert response.status_code == 302  # Redirect after failed login
    assert b'Invalid username or password' in response.data


def test_logout(client):
    # Hash the password before adding the test user to the database
    hashed_password = bcrypt.hashpw('password123'.encode('utf-8'), bcrypt.gensalt())
    test_user = Teammate(username='testuser', password=hashed_password, active=True, is_superuser=False)
    db.session.add(test_user)
    db.session.commit()
    client.post(url_for('login_controller.login'), data={
        'username': 'testuser',
        'password': 'password123'
    })

    response = client.get(url_for('login_controller.logout'))
    assert response.status_code == 302  # Redirect after logout
