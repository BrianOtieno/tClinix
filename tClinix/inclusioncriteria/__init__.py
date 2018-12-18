from flask import Blueprint

blueprint = Blueprint(
    'inclusioncriteria_blueprint',
    __name__,
    url_prefix='/inclusioncriteria',
    template_folder='templates'
)

import tClinix.inclusioncriteria.routes  # noqa: F401
