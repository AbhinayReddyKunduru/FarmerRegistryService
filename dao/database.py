from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:""@host.docker.internal/farmer_registry1', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

