from flask import Blueprint

blueprint = Blueprint(
    'closeout_blueprint',
    __name__,
    url_prefix='/closeout',
    template_folder='templates'
)

import tClinix.closeout.routes  # noqa: F401
