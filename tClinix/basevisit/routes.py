from flask import jsonify, render_template, redirect, request, url_for
from flask_login import login_required
from re import search
import flask_login

from tClinix.basevisit import blueprint


@blueprint.route('/')
@login_required
def index():
    return ("base visits")
