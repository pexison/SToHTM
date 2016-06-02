from flask import Blueprint, json, request, session

from app.models.user import User
from app.utility.encoder import toMd5

user = Blueprint('user', __name__,)

@user.route('/user/create', methods=['POST'])
def create_user():
    email = request.args.get('email')
    fullName = request.args.get('fullName')
    rol = request.args.get('rol')
    password = request.args.get('password')
    if request.args.get('email') is None or len(request.args.get('email')) == 0:
        res = {'error': 'Debe introducir email y password'}
    else:
        if request.args.get('password') is None or len(request.args.get('password')) == 0:
            res = {'error': 'Debe introducir email y password'}
        else:

            UserInstance = User()
            encodedPassword = toMd5(password.encode('utf-8'))
            result = UserInstance.createUser(
                email, fullName, encodedPassword, int(rol))
            res = result

    return json.dumps(res)


@user.route('/user', methods=['GET'])
def get_user():
    id = request.args.get('id')
    UserInstance = User()
    result = UserInstance.getUserById(int(id))[0]
    return json.dumps({'id': result.userId, 'rol': result.rol, 'email': result.email, 'fullName': result.fullname})


@user.route('/users', methods=['GET'])
def get_users():
    UserInstance = User()
    users = UserInstance.getUsers()
    result = []
    for user in users:
        result.append({'id': user.userId, 'fullName': user.fullname,
                       'email': user.email, 'rol': user.rol})

    return json.dumps({'result': result})

@user.route('/user/update', methods=['PUT'])
def update_user():
    email = request.args.get('email')
    password = request.args.get('password')
    fullname = request.args.get('fullName')
    rol = request.args.get('rol')
    UserInstance = User()
    if request.args.get('password') is None or len(request.args.get('password')) == 0:
        newPassword = None
    else:
        newPassword = toMd5(password.encode('utf-8'))
    result = UserInstance.updateUser(email, fullname, newPassword, rol)
    return json.dumps({"updated_user": result})


@user.route('/user/delete', methods=['POST'])
def delete_user():
    userId = request.args.get('userId')
    UserInstance = User()
    result = UserInstance.deleteUser(int(userId))
    return json.dumps({'deleted_user': result})


