from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:root@db:3306/insta_db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


