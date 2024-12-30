from flask import Flask, Blueprint, render_template, request, redirect

index_controller = Blueprint('index_controller', __name__)

@index_controller.route('/')
def index():
    return render_template('login.html')