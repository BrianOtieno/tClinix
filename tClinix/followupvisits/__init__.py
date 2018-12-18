from flask import Blueprint

blueprint = Blueprint(
    'followupvisits_blueprint',
    __name__,
    url_prefix='/flollowupvisits',
    template_folder='templates'
)

import tClinix.followupvisits.routes  # noqa: F401
