from FarmerRegistryService.models.farmer import Farmer
from FarmerRegistryService.models.Fertilizer import Fertilizers
from FarmerRegistryService.models.Pestisides import Pestisides
from FarmerRegistryService.models.User import User_Cred
from FarmerRegistryService.dao.Base import Base
from FarmerRegistryService.app import app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(app, Base)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
