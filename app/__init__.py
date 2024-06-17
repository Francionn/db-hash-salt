from flask import Flask
from infra.repository.user_repository import User_repository


repository = User_repository()
app = Flask(__name__)

from app.controllers import default