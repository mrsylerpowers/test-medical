from datetime import datetime

from flask import request, flash, render_template, redirect, url_for

from test_medical_system.init_app import db
from test_medical_system.authentication.password_protection import encrypt_password, check_encrypted_password
from flask_login import login_user, login_required, current_user, logout_user

from test_medical_system import app, login_manager
from test_medical_system.database.models import User
from test_medical_system.authentication.forms import LoginForm, RegisterForm



@app.route("/register", methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        accesLevel = form.acessType.data
        newUser = User(username=username,password=encrypt_password(password),accessPrivilege=accesLevel)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for("home"))

    from datetime import datetime
    return render_template('register_page.html',currentTime=str(datetime.now()), form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("logout_page"))
    if form.validate_on_submit():
        username = form.username.data
        password_data = form.password.data
        logging_in_user = User.query.filter_by(username=username).first()
        if logging_in_user is not None and check_encrypted_password(password_data, logging_in_user.password):
            login_user(logging_in_user)
            next = request.args.get('next')
            if next is None:
                next = url_for("home")
            flash('Logged in successfully.',"Login")

            return redirect(next)
        else:
            flash('User not found with username and password', "Login")

    from datetime import datetime
    return render_template('login_page.html', currentTime=str(datetime.now()),form=form)

@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout_page():
    if request.method == "POST":
        logout_user()
        return redirect(url_for("login_page"))
    return render_template("logout_page.html")



@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login_page",currentTime=str(datetime.now()), next=request.path))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)