from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta

db=SQLAlchemy()

class Player(db.Model):
    __tablename__='player'
    rank=db.Column(db.SmallInteger,nullable=False,primary_key=True)
    tier=db.Column(db.SmallInteger,nullable=False)
    name=db.Column(db.String(100),nullable=False)
    team=db.Column(db.String(3))
    pos=db.Column(db.String(3),nullable=False)
    pos_rank=db.Column(db.SmallInteger,nullable=False)
    bye=db.Column(db.SmallInteger)
    sos=db.Column(db.String(100))
    ecr_vs_adp=db.Column(db.String(10))