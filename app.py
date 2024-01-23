import json
from flask import Flask, jsonify, request, abort
from models.user import User
from models.phone_number import PhoneNumber
from models.address import Address
from schemas.user import UserSchema
from database import db
from pprint import pprint

# Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/postgres'

# JSON Data
with open('users.json', 'r') as users_file:
    users_list = json.load(users_file)
LAST_ID = 0

# Register the Flask app with SQLAlchemy
db.init_app(app)


@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        user_schema = UserSchema(many=True)
        user_list = user_schema.dump(users)
        return jsonify(user_list)
    except Exception as e:
        abort(500, description=f'Error occurred while retrieving the users: {str(e)}')


@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    phone_numbers_data = user_data.pop("phone_numbers", None)
    address_data = user_data.pop("address", None)

    try:
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()

        if phone_numbers_data:
            for phone_num in phone_numbers_data:
                new_phone_num = PhoneNumber(**phone_num, user_id=new_user.id)
                db.session.add(new_phone_num)
                db.session.commit()
        if address_data:
            for address in address_data:
                new_address = Address(user_id=new_user.id, **address)
                db.session.add(new_address)
                db.session.commit()

        user_schema = UserSchema()
        serialized_user = user_schema.dump(new_user)
        return jsonify({'message': 'New User Added!', 'user': serialized_user}), 200
    except Exception as e:
        db.session.rollback()
        abort(500, description=f"An error occurred while creating a new user: {str(e)}")


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        user_schema = UserSchema()
        serialized_user = user_schema.dump(user)
        return jsonify({'message': f'User with id {user_id}', 'user': serialized_user}), 200
    except ModuleNotFoundError:
        abort(404, description=f'User with id {user_id} not found!')


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        user_schema = UserSchema()
        deleted_user = user_schema.dump(user)

        address_data = deleted_user.get("address", None)
        if address_data:
            for address in address_data:
                Address.query.filter_by(user_id=user_id).delete()
                db.session.commit()

        phone_data = deleted_user.get("phone_numbers", None)
        if phone_data:
            for phone_number in phone_data:
                PhoneNumber.query.filter_by(id=phone_number["id"]).delete()
                db.session.commit()

        User.query.filter_by(id=user_id).delete()
        db.session.commit()

        return jsonify({'message': f'Successfully deleted user {user_id}', 'user': deleted_user}), 200
    except ModuleNotFoundError:
        abort(404, description=f'User with id {user_id} not found!')


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user_data = request.get_json()
    phone_data = updated_user_data.pop("phone_numbers", None)
    address_data = updated_user_data.pop("address", None)
    try:

        if address_data:
            for address in address_data:
                Address.query.filter_by(user_id=user_id).update(address)
                db.session.commit()

        # if phone_data:
        #     for phone_number in phone_data:
        #         PhoneNumber.query.filter_by(id=phone_number["id"]).update(**phone_number)
        #         db.session.commit()

        User.query.filter_by(id=user_id).update(updated_user_data)
        db.session.commit()

        user_schema = UserSchema()
        serialized_user = user_schema.dump(User.query.get_or_404(user_id))
        return jsonify({'message': f'Successfully updated user {user_id}', 'user': serialized_user}), 200
    except Exception as e:
        print(e)
        abort(404, description=f'User with id {user_id} not found!')


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    LAST_ID = max(user['id'] for user in users_list)
    app.run(host='localhost', port=3030)
