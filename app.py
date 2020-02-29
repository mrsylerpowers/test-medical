from flask import Flask, request, flash, render_template, redirect, url_for
from flask_login import LoginManager, login_user, login_required
from models import User, db
from forms import LoginForm
import os

SECRET_KEY = os.urandom(32)
login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
login_manager.init_app(app)
db.init_app(app)

SQLALCHEMY_BINDS = {
    'users': 'sqlite:///medical_test_uid_1.db',
    'patient': 'sqlite:///medical_test_pat_1.db'
}
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS


@app.route('/')
@login_required
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.username.data
        password_data = form.password.data
        logging_in_user = User.query.filter_by(username=data, password=password_data).first()
        if logging_in_user is not None:
            login_user(logging_in_user)
            next = request.args.get('next')
            redirect(url_for(next))
            flash('Logged in successfully.')

    return render_template('login_page.html', form=form)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login_page", next=request.path))


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


if __name__ == '__main__':
    app.run(debug=True)
