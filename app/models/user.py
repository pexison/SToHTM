# -*- coding: utf-8 -*-.

from app.models.db import db

# Declaracion de constantes.
CONST_MAX_USER = 16
CONST_MAX_FULLNAME = 50
CONST_MAX_PASSWORD = 200
CONST_MAX_EMAIL = 30
CONST_MIN_LONG = 1
CONST_MIN_PASSWORD = 1
CONST_MIN_ROL = 1
CONST_MAX_ROL = 2


class User(db.Model):
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
            '<fullname %r, email %r, password %r >' % (
                self.fullname, self.email, self.password)

    def getUsers(self):
        '''Permite obtener todos los usuarios con sus atributos'''

        result = self.query.all()
        return result

    def getUserByEmail(self, email):
        '''Permite buscar un usuario por su correo'''

        long_email = len(email)

        if (long_email > CONST_MAX_EMAIL or long_email < CONST_MIN_LONG):
            return {'status': 'failure', 'reason': '(String) 1 < email < 30'}
        else:
            user = self.query.filter_by(email=email).all()
            return user

    def getUserById(self, id):
        '''Permite buscar un usuario por su id'''

        if (type(id) != int):
            return {'status': 'failure', 'reason': ' Id not integer'}
        else:
            user = self.query.filter_by(userId=id).all()
            return user

    def createUser(self, email, fullname, password, rol):
        '''Permite insertar un usuario'''

        # None checks
        email = email or ""
        fullname = fullname or ""
        password = password or ""
        rol = rol or 0

        ''' Chequeos longitud '''
        checkLongEmail = CONST_MIN_LONG <= len(email) <= CONST_MAX_EMAIL
        checkLongFullname = CONST_MIN_LONG <= len(
            fullname) <= CONST_MAX_FULLNAME
        checkLongPassword = CONST_MIN_PASSWORD <= len(
            password) <= CONST_MAX_PASSWORD

        if not checkLongEmail:
            return {'status': 'failure', 'reason': 'Por favor inserte una dirección de correo electrónico valido'}
        if not checkLongFullname:
            return {'status': 'failure', 'reason': 'Por favor inserte un nombre valido'}
        if not checkLongPassword:
            return {'status': 'failure', 'reason': 'Por favor inserte una contraseña valida'}

        if checkLongEmail and checkLongFullname and checkLongPassword:
            findUser = self.getUserByEmail(email)

            if findUser == []:
                newUser = User(email, fullname, password, rol)
                db.session.add(newUser)
                db.session.commit()
                return {'status': 'success', 'reason': 'Usuario creado'}
            else:
                return {'status': 'failure', 'reason': 'Esta dirección de correo electrónica ya se encuentra registrada'}

    def updateUser(self, email=None, new_fullname=None, new_password=None, new_rol=None):
        '''Permite actualizar los datos de un usuario'''

        # None checks
        email = email or ""
        new_fullname = new_fullname or ""
        new_password = new_password or ""
        new_rol = new_rol or 0

        checkLongEmail = CONST_MIN_LONG <= len(email) <= CONST_MAX_EMAIL

        if (checkLongEmail):
            findUser = self.getUserByEmail(email)

            if findUser != []:

                if new_fullname != "" and new_password != "":
                    checkLongNewFullname = CONST_MIN_LONG <= len(
                        new_fullname) <= CONST_MAX_FULLNAME
                    checkLongNewPassword = CONST_MIN_LONG <= len(
                        new_password) <= CONST_MAX_PASSWORD
                    findUser[0].password = new_password
                    findUser[0].fullname = new_fullname
                    findUser[0].rol = new_rol

                elif new_fullname != "" and new_password == "":
                    checkLongNewFullname = CONST_MIN_LONG <= len(
                        new_fullname) <= CONST_MAX_FULLNAME
                    findUser[0].fullname = new_fullname
                    findUser[0].rol = new_rol

                elif new_fullname == "" and new_password != "":
                    checkLongNewPassword = CONST_MIN_LONG <= len(
                        new_password) <= CONST_MAX_PASSWORD
                    findUser[0].password = new_password
                    findUser[0].rol = new_rol

                else:
                    return {'status': 'failure', 'reason': ' Name or password should be != None '}

                db.session.commit()

                return {'status': 'success', 'reason': 'User updated'}

            else:
                return {'status': 'failure', 'reason': 'Couldnt find user :( '}

        return {'status': 'failure', 'reason': 'Email too long'}

    def deleteUser(self, id):
        '''Permite eliminar un usuario'''

        findUser = self.getUserById(id)
        if findUser != []:
            for i in findUser:
                self.query.filter_by(userId=id).delete()
            db.session.commit()
            return {'status': 'success', 'reason': 'User deleted'}

        return {'status': 'failure', 'reason': 'Couldnt find user :('}
