from collections import Counter
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import login_required
from re import search
import flask_login
from tClinix.inclusioncriteria import blueprint

from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

@blueprint.route('/', methods=['GET', 'POST'])
def login():
    return "entered inclusion criteria"
