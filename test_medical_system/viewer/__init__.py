from flask import Blueprint

from test_medical_system import app

patent = Blueprint('patent', __name__,url_prefix='/patent',
                    template_folder='templates',
                    static_folder='static')

import test_medical_system.viewer.paisent_viewer
import test_medical_system.viewer.account_balance_viewer

app.register_blueprint(patent)

