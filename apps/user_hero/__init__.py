from flask import Blueprint

hero = Blueprint('user_hero', __name__)
from . import controller

