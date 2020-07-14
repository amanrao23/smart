from flask import render_template,request,Blueprint,url_for, redirect
from flask_login import  login_user, current_user
control=Blueprint('control',__name__)
from app.control.forms import Newctrlcntrform,Loginctrlform
from app import db,login_manager
from app.models import Control,Allusers
from functools import wraps


def login_required(role="admin"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if ((current_user.role != role) and (role != "admin")):
                return login_manager.unauthorized()
            return fn(*args, **kwargs)

        return decorated_view

    return wrapper


@control.route('/registercontrol', methods=['GET', 'POST'])  # registration of a control centre
def registercontrol():
    form = Newctrlcntrform()
    if form.validate_on_submit():
        newuser = Allusers(username=form.username.data, password=form.password.data, role='admin')
        new_centre = Control(c_name=form.name.data, c_username=form.username.data, c_password=form.password.data)
        db.session.add(new_centre)
        db.session.add(newuser)
        db.session.commit()
        return redirect(url_for('control.logincontrol'))
    return render_template('registercontrol.html', form=form)


@control.route('/logincontrol', methods=['GET', 'POST'])  # login of a control centre
def logincontrol():
    form = Loginctrlform()
    if form.validate_on_submit():
        # return form.username.data + ' ' + form.password.data
        user = Allusers.query.filter_by(username=form.username.data).first()
        controluser = Control.query.filter_by(c_username=form.username.data).first()
        if user and controluser:
            if (user.password == form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('control.dashboard'))
        return '<h1>Invalid username or password</h1>'
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    return render_template('login.html', form=form)


@control.route('/dashboard')
@login_required(role="admin")
def dashboard():
    return render_template('dashboard.html', name=current_user.username)
