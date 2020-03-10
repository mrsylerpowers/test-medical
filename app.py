from flask import request, flash, render_template, redirect, url_for
from password_protection import encrypt_password, check_encrypted_password
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

from models import User
from forms import LoginForm, RegisterForm
from create_db import create_app, db


app = create_app()

login_manager = LoginManager()

login_manager.init_app(app)



@app.route('/')
@login_required
def hello_world():
    return 'Hello World!'

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

    return render_template('register_page.html', form=form)

@login_required
@app.route("/logout", methods=['GET', 'POST'])
def logout_page():
    if request.method == "POST":
        logout_user()
        return redirect(url_for("login_page"))
    return render_template("logout_page.html")

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
            flash('Logged in successfully.',"Login")

            return redirect(next)
        else:
            flash('User not found with username and password', "Login")

    return render_template('login_page.html', form=form)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login_page", next=request.path))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == '__main__':
    app.run(debug=True)
