from flask import jsonify, render_template, redirect, request, url_for
from flask_login import login_required
from re import search
import flask_login

from tClinix import db, login_manager
from tClinix.base import blueprint

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return "login form"
