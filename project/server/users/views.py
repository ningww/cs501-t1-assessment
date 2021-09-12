from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

import json
import datetime

users_blueprint = Blueprint('users', __name__)

class UsersAPI(MethodView):
    def get(self):
        try:
            user_list = User.query.all()
            responseObject = []
            for user in user_list:
                responseObject.append({
                    "id": user.id,
                    "email": user.email,
                    "password": user.password,
                    "registered_on": user.registered_on.strftime("%a, %d %b %Y %H:%M:%S %Z"),
                    "admin": user.admin
                })
            return make_response(json.dumps(responseObject)), 201
        except:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401

# define the API resources
users_view = UsersAPI.as_view('users_api')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=users_view,
    methods=['GET']
)