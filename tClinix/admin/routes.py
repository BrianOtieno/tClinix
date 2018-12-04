from flask import jsonify, render_template, redirect, request, url_for
from flask_login import login_required
from re import search
from tClinix.admin import blueprint

from bcrypt import checkpw
from flask import (
    current_app,
    jsonify,
    redirect,
    render_template,
    request,
    url_for
)

from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from tClinix.admin.forms import (
    AddUser,
    CreateAccountForm,
    LoginForm,
)

@blueprint.route('/', methods=['GET', 'POST'])
def login():
    return render_template(
        'login.html',
        login_form=LoginForm(request.form),
        create_account_form=CreateAccountForm(request.form)
    )
    if request.method == 'POST':
        name = str(request.form['name'])
        password = str(request.form['password'])
        user = db.session.query(User).filter_by(name=name).first()
        if user:
            if current_app.production:
                hash = current_app.vault_client.read(
                    f'secret/data/user/{name}'
                )['data']['data']['password'].encode('utf-8')
            else:
                hash = user.password.encode('utf-8')
            if checkpw(password.encode('utf8'), hash):
                login_user(user)
                return redirect(url_for('base_blueprint.dashboard'))

        return render_template('errors/page_403.html')
    if not current_user.is_authenticated:
        return render_template(
            'login.html',
            login_form=LoginForm(request.form),
            create_account_form=CreateAccountForm(request.form)
        )
    return redirect(url_for('base_blueprint.dashboard'))
