from datetime import datetime

from app import db
import enum


class TabStatus(enum.Enum):
    PENDING = 1
    ACTIVE = 2
    INACTIVE = 3


class Tab(db.Model):
    """
        Model for Keeping track of tabs
    """
    __tablename__ = 'tabs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, )
    created_by = db.Column(db.Integer, nullable=False, unique=False)
    status = db.Column(db.Enum(TabStatus), nullable=False, unique=False)
    creation_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_modified_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow,
                                   onupdate=datetime.utcnow)
