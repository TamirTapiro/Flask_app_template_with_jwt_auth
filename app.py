from flask import Flask, jsonify, request
from extentions import jwt
from auth.auth_manager import auth_manager_blueprint
import config


def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY 
    jwt.init_app(app)
    app.register_blueprint(auth_manager_blueprint, url_prefix='/api/auth')
    return app