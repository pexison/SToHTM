# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo model.py
sys.path.append('app/models')

from model import *

# Declaracion de constantes.
CONST_MAX_USER     = 16
CONST_MAX_FULLNAME = 50
CONST_MAX_PASSWORD = 200
CONST_MAX_EMAIL    = 30
CONST_MIN_LONG     = 1
CONST_MIN_PASSWORD = 1


class user(object):
    '''Clase que permite manejar a los usuarios'''
    
    def getAllUsers(self):
        '''Permite obtener todos los usuarios con sus atributos'''
        
        result = classUser.query.all()
        return result

    def searchUser(self,email):
        '''Permite buscar un usuario por su correo'''
        
        if (type(email) != str):
            return []
        else:
            long_email = len(email)
            if (long_email >CONST_MAX_EMAIL or long_email < CONST_MIN_LONG):
                return []
            else:
                user = classUser.query.filter_by(email = email).all()
                return user
 
 
    def insertUser(self, email, fullname, password):
        '''Permite insertar un usuario'''
        
        checkEmail    = type(email) == str
        checkName     = type(fullname) == str
        checkPassword = type(password) == str
        
        if checkEmail and checkName and checkPassword:
            checkLongEmail    = CONST_MIN_LONG <= len(email) <= CONST_MAX_EMAIL
            checkLongFullname = CONST_MIN_LONG <= len(fullname) <= CONST_MAX_FULLNAME
            checkLongPassword = CONST_MIN_PASSWORD <= len(password) <=  CONST_MAX_PASSWORD

            if  checkLongEmail and checkLongFullname and checkLongPassword:
                findUser = self.searchUser(email)

                if findUser == []:
                    newUser = classUser(email,fullname,password)
                    db.session.add(newUser)
                    db.session.commit()
                    return True
        return False
        

    def updateUser(self, email, new_fullname, new_password):   
        '''Permite actualizar los datos de un usuario'''  
        
        checkEmail       = type(email) == str
        checkNewFullname = type(new_fullname) == str
        checkNewPassword = type(new_password) == str

        if checkEmail and checkNewFullname and checkNewPassword:
            checkLongEmail       = CONST_MIN_LONG <= len(email) <= CONST_MAX_EMAIL
            checkLongNewFullname = CONST_MIN_LONG <= len(new_fullname) <= CONST_MAX_FULLNAME
            checkLongNewPassword = CONST_MIN_LONG <= len(new_password) <=  CONST_MAX_PASSWORD
 
            if checkLongEmail and checkLongNewFullname and checkLongNewPassword:
                findUser = self.searchUser(email)       
         
                if findUser != []:
                    findUser[0].fullname = new_fullname
                    findUser[0].password = new_password
                    db.session.commit()
                    return True
        return False    
     
     
    def deleteUser(self,email):
        '''Permite eliminar un usuario'''
        
        checkEmail = type(email) == str  
        
        if checkEmail:
            checkLongEmail = CONST_MIN_LONG <= len(email) <= CONST_MAX_EMAIL

            if checkLongEmail: 
                findUser = self.searchUser(email) 

                if findUser != []: 
                    for i in findUser:    
                        db.session.delete(i)
                    db.session.commit()
                    return True
        return False
        
# Fin Clase user