from FarmerRegistryService.dao.Base import Base
from FarmerRegistryService.dao.database import engine
from sql_db import db


class Pestisides(db.Model):
    __tablename__ ="Pestisides"
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))
    unit_cost = db.Column(db.Float)
    supplier = db.Column(db.String(200))
    unit_quantity = db.Column(db.Float)
    cottons = db.Column(db.Integer)
    total_cost = db.Column(db.Float)

    def __init__(self, product_name, unit_cost, supplier, unit_quantity, cottons, total_cost):
        self.unit_cost = unit_cost
        self.product_name = product_name
        self.total_cost = total_cost
        self.supplier = supplier
        self.unit_quantity = unit_quantity
        self.cottons = cottons

    def __repr__(self):
        return " <Product name='%s',unit_costr='%s', total_cost='%s',supplier='%s', " \
               "unit_quantity='%s'," \
               "cottons='%s>" %(self.product_name,self.unit_cost,self.total_cost,self.supplier,self.unit_quantity,self.cottons)
Base.metadata.create_all(bind=engine)