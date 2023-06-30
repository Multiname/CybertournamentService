from flask import Blueprint

moderators = Blueprint('moderators', __name__)

from . import api