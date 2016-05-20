# -*- coding: utf-8 -*-.

import sys
sys.path.append('app/models')
from db import *


# Declaracion de constantes.
CONST_MAX_USER = 16
CONST_MAX_FULLNAME = 50
CONST_MAX_PASSWORD = 200
CONST_MAX_EMAIL = 30
CONST_MIN_LONG = 1
CONST_MIN_PASSWORD = 1
CONST_MIN_ROL=1
CONST_MAX_ROL=2


class User (db.Model):
    '''Clase que define el modelo Usuario'''

    __tablename__ = 'user'
    userId = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String(30), unique=True)
    fullname = db.Column(db.String(50))
    password = db.Column(db.String(200))
    rol = db.Column(db.Integer)

    def __init__(self, email=None, fullname=None, password=None, rol=None):
        '''Constructor del modelo usuario'''
        self.email = email
        self.fullname = fullname
        self.password = password
        self.rol = rol

    def __repr__(self):
        '''Representacion en string del modelo Usuario'''
        return \
            '<fullname %r, email %r, password %r >' % (self.fullname, self.email, self.password)

    def getUsers(self):
        '''Permite obtener todos los usuarios con sus atributos'''

        result = self.query.all()
        return result

    def getUserByEmail(self, email):
        '''Permite buscar un usuario por su correo'''

        long_email = len(email)

        if (long_email > CONST_MAX_EMAIL or long_email < CONST_MIN_LONG):
            return {'status': 'failed', 'reason': '(String) 1 < email < 30'}
        else:
            user = self.query.filter_by(email=email).all()
            return user

    def getUserById(self, id):
        '''Permite buscar un usuario por su id'''

        if (type(id) != int):
            return {'status': 'failed', 'reason': ' Id not integer'}
        else:
            user = self.query.filter_by(userId=id).all()
            return user

    def createUser(self, email, fullname, password, rol):
        '''Permite insertar un usuario'''

        ''' Chequeos longitud '''
        checkLongEmail = CONST_MIN_LONG <= len(email) <= CONST_MAX_EMAIL
        checkLongFullname = CONST_MIN_LONG <= len(fullname) <= CONST_MAX_FULLNAME
        checkLongPassword = CONST_MIN_PASSWORD <= len(password) <= CONST_MAX_PASSWORD

        if checkLongEmail and checkLongFullname and checkLongPassword:
            findUser = self.getUserByEmail(email)

            if findUser == []:
                newUser = User(email, fullname, password, rol)
                db.session.add(newUser)
                db.session.commit()
                return {'status': 'success', 'reason': 'Usuario creado'}
            else:
                return {'status': 'failed', 'reason': 'El usuario ya existe'}

        return {'status': 'failed', 'reason': 'Check failed, 1 < Email < 30 - 1 < fullname < 50 - 1 < pass < 200'}

    def updateUser(self, email=None, new_fullname=None, new_password=None, new_rol=None):
        '''Permite actualizar los datos de un usuario'''

        checkLongEmail = CONST_MIN_LONG <= len(email) <= CONST_MAX_EMAIL


        if (checkLongEmail):
            findUser = self.getUserByEmail(email)

            if findUser != []:

                if new_fullname != None and new_password != None:
                    checkLongNewFullname = CONST_MIN_LONG <= len(new_fullname) <= CONST_MAX_FULLNAME
                    checkLongNewPassword = CONST_MIN_LONG <= len(new_password) <= CONST_MAX_PASSWORD
                    findUser[0].password = new_password
                    findUser[0].fullname = new_fullname
                    findUser[0].rol = new_rol

                elif new_fullname != None and new_password == None:
                    checkLongNewFullname = CONST_MIN_LONG <= len(new_fullname) <= CONST_MAX_FULLNAME
                    findUser[0].fullname = new_fullname
                    findUser[0].rol = new_rol

                elif new_fullname == None and new_password != None:
                    checkLongNewPassword = CONST_MIN_LONG <= len(new_password) <= CONST_MAX_PASSWORD
                    findUser[0].password = new_password
                    findUser[0].rol = new_rol

                else:
                    return {'status': 'failed', 'reason': ' Name or password should be != None '}

                db.session.commit()

                return {'status': 'success', 'reason': 'User updated'}

            else:
                return {'status': 'failed', 'reason': 'Couldnt find user :( '}

        return {'status': 'failed', 'reason': 'Email too long'}

    def deleteUser(self, id):
        '''Permite eliminar un usuario'''

        findUser = self.getUserById(id)
        if findUser != []:
            for i in findUser:
                self.query.filter_by(userId=id).delete()
            db.session.commit()
            return {'status': 'success', 'reason': 'User deleted'}
        else:
            {'status': 'failed', 'reason': 'Couldnt find user :('}

        return {'status': 'failed', 'reason': 'Couldnt find user :('}
