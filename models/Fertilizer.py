from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Fertilizers(Base):
    __tablename__ = "Fertilizers"
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(300))
    unit_cost = Column(Float)
    supplier = Column(String(100))
    quantity = Column(Float)
    bags = Column(Integer)
    total_cost = Column(Float)

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