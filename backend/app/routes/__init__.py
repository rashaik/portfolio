from flask import Blueprint

bp = Blueprint('main', __name__)

from . import projects, skills, auth
