from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from  flask_migrate import Migrate, migrate
from flask_seeder import FlaskSeeder

app=Flask(__name__)
app.config.from_object("config")


db = SQLAlchemy()
migrate = Migrate()
seeder =  FlaskSeeder()

def createApp():
    db.init_app(app)
    migrate.init_app(app,db)
    seeder.init_app(app,db)


    with app.app_context():
        from . import models
        #include api route
        from . import apis
       

        return app

