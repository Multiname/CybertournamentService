from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy()
db.init_app(app)
migrage = Migrate(app, db)

from .players import players as players_blueprint
from .moderators import moderators as moderators_blueprint
app.register_blueprint(players_blueprint, url_prefix='/players')
app.register_blueprint(moderators_blueprint, url_prefix='/moderators')