from flask import Blueprint

blueprint = Blueprint(
    'scheduledvisits_blueprint',
    __name__,
    url_prefix='/scheduledvisits',
    template_folder='templates'
)

import tClinix.scheduledvisits.routes  # noqa: F401
