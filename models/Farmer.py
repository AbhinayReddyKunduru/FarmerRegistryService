from FarmerRegistryService.dao.Base import Base
from FarmerRegistryService.dao.database import engine
from sql_db import db
class Farmer(db.Model):
    __tablename__ = "farmer"
    farmer_id = db.Column(db.Integer, primary_key=True)
    farmer_name = db.Column(db.String(100), unique=True) #changed username to farmer_name wont work unti lwe change the database.
    mobile_number = db.Column(db.String(100), unique=True)
    village_name = db.Column(db.String(100))
    address = db.Column(db.String(250))

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

Base.metadata.create_all(bind=engine)

