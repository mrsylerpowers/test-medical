from flask import url_for, redirect
from flask_login import LoginManager, login_required, current_user

from test_medical_system.database.models import User
from test_medical_system.init_app import create_app

app = create_app()

login_manager = LoginManager()

login_manager.init_app(app)

# Modules  we want to have routed
# Isn't this circular????

import test_medical_system.authentication.authentication_handlers
import test_medical_system.viewer

@app.route('/')
@login_required
def home():
    if current_user.accessPrivilege > 0:
        return redirect(url_for("patent.viewPaisentList"))
    elif current_user.accessPrivilege == 0:
        return redirect(url_for("accountBalancePatent"))

    return 'Hello World!'
