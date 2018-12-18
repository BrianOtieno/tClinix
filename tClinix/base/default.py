from importlib.util import spec_from_file_location, module_from_spec
from sqlalchemy import Boolean, Float, Integer, PickleType

from tClinix import db
from tClinix.admin.models import User
from tClinix.base.custom_base import factory


def create_default_user():
    factory(User, **{
        'name': 'OBrien',
        'email': 'gebryo@intelligencia.com',
        'password': 'cisco'
    })
