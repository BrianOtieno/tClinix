from flask import Blueprint

blueprint = Blueprint(
    'labresults_blueprint',
    __name__,
    url_prefix='/labresults',
    template_folder='templates'
)

import tClinix.labresults.routes  # noqa: F401
