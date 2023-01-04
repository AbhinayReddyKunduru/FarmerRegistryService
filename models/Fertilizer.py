from FarmerRegistryService.dao.Base import Base
from FarmerRegistryService.dao.database import engine
from sql_db import db


class Fertilizers(db.Model):
    __tablename__ = "Fertilizers"
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(300))
    unit_cost = db.Column(db.Float)
    supplier = db.Column(db.String(100))
    quantity = db.Column(db.Float)
    bags = db.Column(db.Integer)
    total_cost = db.Column(db.Float)

    def __init__(self, product_name, unit_cost, supplier, quantity, bags, total_cost):
        self.product_name = product_name
        self.unit_cost = unit_cost
        self.supplier = supplier
        self.quantity = quantity
        self.bags = bags
        self.total_cost = total_cost

    def __repr__(self):
        return "<Fertilizers(name='%s',unit_cost='%s',supplier='%s',quantity='%s', " \
               "bags='%s',total_cost='%s')>"%(self.product_name,self.unit_cost,self.supplier,self.quantity,self.bags,self.total_cost)

Base.metadata.create_all(bind=engine)