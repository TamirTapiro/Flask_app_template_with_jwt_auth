from flask import Blueprint, request, make_response
from flask.json import jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from extentions import users_collection
from dataclasses import FrozenInstanceError
from models.user import User

auth_manager_blueprint = Blueprint('auth_manager', __name__)



@auth_manager_blueprint.route('/login', methods=['POST'])
def login():
    email, password = request.get_json().get('email', None), request.get_json().get('password', None)
    if email is None or password is None:
        return jsonify({'message': 'request must have a valid email and password'}), 401
    try:
        user_json = users_collection.find_one({'$and': [{'email': email}, {'password': password}]})
        user = User(**user_json)

        if user is None:
            return jsonify({'message': 'email or password are incorect'}), 404
        else:
            access_token = create_access_token(identity=str(user._id))
            return jsonify(access_token=access_token)
    except:
        return jsonify({'message': 'Oops! somthing went wrong.'}), 404

@auth_manager_blueprint.route('/register', methods=['POST'])
def register():
    cred = request.get_json()
    if 'email' not in cred or 'password' not in cred:
        return jsonify({'message': 'body must have email and password feilds'}), 401
    try:
        user = User(**cred)
        db_result =  users_collection.find_one({'email': user.email})
        if db_result is None:
            users_collection.insert_one(user.__dict__)
            return jsonify(f'{user.email} has been registered succefully'), 200 
        else:
            return jsonify(f'user {user.email} already exists in the system'), 409

    except TypeError as typeErr:
        return jsonify({'message': str(typeErr).replace("__init__()", "")}), 400
    except FrozenInstanceError as instErr:
        return jsonify({'message': str(instErr).replace("__init__()", "")}), 400


