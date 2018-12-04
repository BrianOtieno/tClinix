from bcrypt import gensalt, hashpw
from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from threading import Thread

from tClinix import db , scheduler
from tClinix.base.custom_base import CustomBase


class User(CustomBase, UserMixin):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    type = Column(String, default='admin')
    name = Column(String(120), unique=True)
    email = Column(String(120), unique=True)
    access_rights = Column(String(120))
    password = Column(String(30))
    # tasks = relationship('Task', back_populates='user')

    def update(self, **kwargs):
        hash = hashpw(kwargs.pop('password').encode('utf8'), gensalt())
        if current_app.production:
            current_app.vault_client.write(
                f'secret/data/user/{kwargs["name"]}',
                data={'password': hash.decode('utf-8')}
            )
        else:
            kwargs['password'] = hash.decode('utf-8')
        super().update(**kwargs)

    def __repr__(self):
        return self.name
