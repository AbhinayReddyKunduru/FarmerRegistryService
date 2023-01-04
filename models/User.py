from FarmerRegistryService.dao.Base import Base
from FarmerRegistryService.dao.database import engine
from sql_db import db


class UserCred(db.Model):
    __tablename__ = "user__cred"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User(email='%s', password='%s')>" % (
            self.email,
            self.password)


Base.metadata.create_all(bind=engine)