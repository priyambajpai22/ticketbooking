import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from src.model import User
from app.settings import app, db
from app.data_prepopulate import prepopulate


#app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    db.create_all()
    prepopulate()
    manager.run()