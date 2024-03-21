import sqlalchemy as sa
from sqlalchemy.sql import func
from sqlalchemy_history import make_versioned

import flaskr.config_app as ca
from flaskr.db import db_instance, db_persist

make_versioned(user_cls='TokenBlocklistModel')


class TokenBlocklistModel(db_instance.Model):
    __versioned__ = {}
    __tablename__ = 'token_block_list'
    __table_args__ = {"schema": ca.DEFAULT_DB_SCHEMA}

    id = db_instance.Column(db_instance.Integer, primary_key=True)
    jti = db_instance.Column(db_instance.String(36), nullable=False, index=True)
    created_at = db_instance.Column(db_instance.DateTime(timezone=True), nullable=False, default=func.now())

    @classmethod
    def get_token(cls, jti):
        return db_instance.session.query(TokenBlocklistModel.id).filter_by(jti=jti).scalar()

    @db_persist
    def save(self):
        db_instance.session.add(self)


sa.orm.configure_mappers()
