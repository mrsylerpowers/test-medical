from datetime import datetime

from flask_login import login_required, current_user
from flask import abort, render_template

from test_medical_system import app


@app.route("/account/balance")
@login_required
def accountBalancePatent():
    if current_user.accessPrivilege != 0:
        return abort(401)

    return render_template("account_balance_html.html", current_user=current_user, accountBalance=current_user.patentInfo.accountBalance,currentTime=str(datetime.now()))

