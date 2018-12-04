from flask import Blueprint

blueprint = Blueprint(
    'recruitment_blueprint',
    __name__,
    url_prefix='/recruitment',
    template_folder='templates'
)

import tClinix.recruitment.routes  # noqa: F401
