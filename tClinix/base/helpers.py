from sqlalchemy import exc

from tClinix import db, scheduler


def retrieve(model, **kwargs):
    return db.session.query(model).filter_by(**kwargs).first()
