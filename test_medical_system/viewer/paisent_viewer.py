from flask import request, flash, render_template, redirect, url_for, abort

from test_medical_system.init_app import db
from test_medical_system.authentication.password_protection import encrypt_password, check_encrypted_password
from flask_login import login_user, login_required, current_user, logout_user

from test_medical_system import app, login_manager
from test_medical_system.database.models import User, Patent
from test_medical_system.viewer import patent
from test_medical_system.viewer.forms import RegisterFormPatent

from datetime import datetime



@patent.route("/create", methods=['GET', 'POST'])
@login_required
def createPatent():
    if current_user.accessPrivilege != 1:
        return abort(401)
    form = RegisterFormPatent()
    if form.validate_on_submit():
        patent = Patent(name=form.name.data,address=form.address.data,phoneNumber=form.mobile_phone.data, accountBalance=form.accountBalance.data)
        user = User(username=form.username.data,password=encrypt_password(form.password.data),accessPrivilege=0,patentInfo=patent)
        db.session.add(user)
        db.session.add(patent)
        db.session.commit()
        flash("Successfully Created Patent: "+  form.name.data)
        return redirect(url_for("patent.viewPaisentList"))
    return render_template("patent_create.html", current_user=current_user,currentTime=str(datetime.now()), form=form)

@patent.route("/view")
@login_required
def viewPaisentList():
    if current_user.accessPrivilege < 1:
        return abort(401)

    return render_template("patent_view.html", current_user=current_user, patents=Patent.query.all(),currentTime=str(datetime.now()))


@patent.route("/view/<paient_id>" , methods=['GET', 'POST'])
@login_required
def viewPaisent(paient_id):
    if current_user.accessPrivilege < 1:
        return abort(401)
    patent = db.session.query(Patent).filter(Patent.id == paient_id).one()
    user = patent.user

    form = RegisterFormPatent(username=user.username, password="*********", name=patent.name, accountBalance=patent.accountBalance, mobile_phone=patent.phoneNumber, address=patent.address)



    if form.validate_on_submit():
        patent = db.session.query(Patent).filter(Patent.id == paient_id).one()
        user = patent.user
        user.username = form.username.data
        patent.name = form.name.data
        patent.accountBalance = form.accountBalance.data
        patent.phoneNumber = form.mobile_phone.data
        patent.address = form.address.data
        db.session.commit()
        flash("Successfully Edited User")
        return redirect(url_for("patent.viewPaisentList"))

    return render_template("patent_edit.html", current_user=current_user, form=form,currentTime=str(datetime.now()))

