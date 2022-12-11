from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class Farmer(Base):
    __tablename__ = "Farmer"
    farmer_id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    mobile_number = Column(String(100), unique=True)
    village_name = Column(String(100))
    address = Column(String(250))

    def __init__(self, username, mobile_number, village_name, address):
        self.username = username
        self.mobile_number = mobile_number
        self.village_name = village_name
        self.address = address

    def __repr__(self):
        return "<Farmer(username='%s', mobile_number='%s', village_name='%s', address='%s')>" % (
            self.username,
            self.mobile_number,
            self.village_name,
            self.address,
        )