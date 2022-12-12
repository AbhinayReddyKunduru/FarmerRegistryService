from sqlalchemy import Column,Integer,Float,String
from services.Base import Base

class Pestisides(Base):
    __tablename__ ="Pestisides"
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(200))
    unit_cost = Column(Float)
    supplier = Column(String(200))
    unit_quantity = Column(Float)
    cottons = Column(Integer)
    total_cost = Column(Float)

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