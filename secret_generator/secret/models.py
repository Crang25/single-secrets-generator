import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from secret_generator.store.database.models import db


class Secret(db.Model):
    __tablename__ = 'secret'

    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    created = db.Column(
        db.DateTime(),
        server_default=datetime.now().replace(tzinfo=timezone.utc).astimezone(tz=None).strftime("%m/%d/%Y, %H:%M:%S"),
        nullable=False
    )
    secret_key = relationship('SecretKey', back_populates='secret', uselist=False)
    secret_code = relationship('SecretCode', back_populates='secret', uselist=False)


class SecretKey(db.Model):
    __tablename__ = 'secretcode'

    id = db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.Text(), nullable=False)
    secret = db.Column(db.Integer(), db.ForeignKey('secret.id', ondelete='CASCADE'), nullable=False)


class SecretCode(db.Model):
    __tablename__ = 'secretkey'

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    secret = db.Column(db.Integer(), db.ForeignKey('secret.id', ondelete='CASCADE'), nullable=False)
