#!/usr/bin/env python3

from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api
from models import User, Recipe, UserSchema, RecipeSchema


class Signup(Resource):
    def post(self):
        data = request.get_json()
        errors = []

        username = data.get('username')
        password = data.get('password')
        image_url = data.get('image_url')
        bio = data.get('bio')

        if not username:
            errors.append("Username is required.")
        if not password:
            errors.append("Password is required.")

        if errors:
            return {"errors": errors}, 422

        user = User(username=username, image_url=image_url, bio=bio)
        try:
            user.password_hash = password  # Trigger the setter
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {'errors': ["Username must be unique."]}, 422
        except ValueError as e:
            db.session.rollback()
            return {'errors': [str(e)]}, 422

        session['user_id'] = user.id
        return UserSchema().dump(user), 201


class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            if user:
                return UserSchema().dump(user), 200
        return {'error': 'Unauthorized'}, 401


class Login(Resource):
    pass


class Logout(Resource):
    pass


class RecipeIndex(Resource):
    pass


api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
