from flask import Blueprint

blueprint = Blueprint(
    'radiology_blueprint',
    __name__,
    url_prefix='/radiology',
    template_folder='templates'
)

import tClinix.radiology.routes  # noqa: F401
