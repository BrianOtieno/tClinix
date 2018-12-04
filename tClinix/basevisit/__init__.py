from flask import Blueprint

blueprint = Blueprint(
    'basevisit_blueprint',
    __name__,
    url_prefix='/basevisit',
    template_folder='templates'
)

import tClinix.basevisit.routes  # noqa: F401
