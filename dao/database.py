from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

engine = create_engine('mysql+pymysql://root:""@host.docker.internal/farmer_registry1', pool_pre_ping=True)
# url_object = URL.create(
#
#     "mysql+pymysql",
#     username="root",
#     password="",
#     host="db",
#     database="farmer_registry1",
#     port=3306
#                 )
# engine = create_engine(url_object)
Session = sessionmaker(bind=engine)
session = Session()

# docker minikude (cuberbetics)