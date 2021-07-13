from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from  flask_migrate import Migrate, migrate
from flask_seeder import FlaskSeeder
from flask_marshmallow import Marshmallow
from flask_cors import CORS



app=Flask(__name__)
app.config.from_object("config")
CORS(app)

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
seeder =  FlaskSeeder()

def createApp():
    db.init_app(app)
    migrate.init_app(app,db)
    ma.init_app(app)
    seeder.init_app(app,db)


    with app.app_context():
        from . import models 
        #include api rou te
        from . import apis
       

        return app

