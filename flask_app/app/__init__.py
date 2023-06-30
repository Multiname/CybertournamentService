from flask import Flask

app = Flask(__name__)

from .players import players as players_blueprint
from .moderators import moderators as moderators_blueprint
app.register_blueprint(players_blueprint, url_prefix='/players')
app.register_blueprint(moderators_blueprint, url_prefix='/moderators')