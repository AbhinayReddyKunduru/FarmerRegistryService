from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:''@localhost/farmer_registry1', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
