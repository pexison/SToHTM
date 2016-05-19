from flask import Blueprint, json, request

from app.models.user import User

user = Blueprint('user', __name__, url_prefix='/api')


@user.route('/user/create', methods=['POST'])
def create_user():
    params = request.args
    email = params.get('email', '')
    fullname = params.get('fullname', '')
    password = params.get('password', '')
    UserInstance = User()
    result = UserInstance.insertUser(email, fullname, password)
    return json.dumps({'user_created': result})


@user.route('/user/<id>', methods=['POST'])
def get_user(id):
    UserInstance = User()
    result = UserInstance.getUserById(int(id))[0]
    return json.dumps({'email': result.email, 'fullname': result.fullname})


@user.route('/user/<id>/update', methods=['PUT'])
def update_user(id):
    params = request.args
    email = params.get('email', None)
    fullname = params.get('fullname', None)
    password = params.get('password', None)
    UserInstance = User()
    result = UserInstance.updateUser(email=email, password=password,
                                     fullname=fullname)[0]
    return json.dumps({"updated_user": result})


@user.route('/user/<id>/delete', methods=['POST'])
def delete_user(id):
    UserInstance = User()
    result = UserInstance.deleteUser(int(id))
    return json.dumps({'deleted_user': result})
