from sqlalchemy import Column,Integer,String
from FarmerRegistryService.dao.Base import Base
from FarmerRegistryService.dao.database import engine

class UserCred(Base):
    __tablename__ = "user__cred"
    user_id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column(String(150), unique=True)
    password = Column(String(150))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User(email='%s', password='%s')>" % (
            self.email,
            self.password)

Base.metadata.create_all(bind=engine)