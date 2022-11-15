from flask import Blueprint

squad = Blueprint('user_squad', __name__)
from . import controller

