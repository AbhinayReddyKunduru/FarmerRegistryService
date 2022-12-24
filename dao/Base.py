from sqlalchemy.ext.declarative import declarative_base
from FarmerRegistryService.dao.database import engine

Base = declarative_base(bind=engine)



