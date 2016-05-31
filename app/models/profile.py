# -*- coding: utf-8 -*-.

from app.models.db import db
from app.models.user import User



class Profile(db.Model):
    '''Clase que define el modelo Usuario'''

    __tablename__ = 'profile'
    perfilId    = db.Column(db.Integer, primary_key=True, index=True)
    email       = db.Column(db.String(30), db.ForeignKey('user.email'))
    sexo        = db.Column(db.String(20))
    edad        = db.Column(db.Integer)
    vision      = db.Column(db.String(300))
    habilidades = db.Column(db.String(300))
    destrezas   = db.Column(db.String(300))
    formacion   = db.Column(db.String(30))
    experiencia = db.Column(db.String(300))
    cursos      = db.Column(db.String(300))
    talleres    = db.Column(db.String(300))
    seminarios  = db.Column(db.String(300))
    ponencias   = db.Column(db.String(300))
    publicaciones = db.Column(db.String(300))
    becas      = db.Column(db.String(300))


    def __init__(self, email=None, sexo=None, edad=None, vision=None,
                habilidades=None, destrezas=None, formacion=None, 
                experiencia=None, cursos=None, talleres=None,
                seminarios=None, ponencias=None, publicaciones=None,
                becas=None):

        '''Constructor del modelo usuario'''
        self.email          = email
        self.sexo           = sexo 
        self.edad           = edad 
        self.vision         = vision 
        self.habilidades    = habilidades 
        self.destrezas      = destrezas 
        self.formacion      = formacion 
        self.experiencia    = experiencia 
        self.cursos         = cursos 
        self.talleres       = talleres 
        self.seminarios     = seminarios 
        self.ponencias      = ponencias 
        self.publicaciones  = publicaciones 
        self.becas          = becas


    def __repr__(self):
        '''Representacion en string del modelo Perfil'''
        return \
            '< email %r, sexo %r, edad %r (incompleto)>' % (
                self.email, self.sexo, self.edad)

    def getProfileById(self, id):
        '''Permite buscar un usuario por su id'''

        if (type(id) != int):
            return {'status': 'failure', 'reason': ' Id not integer'}
        else:
            profile = self.query.filter_by(perfilId=id).all()
            return profile

    def createProfile(self, email, sexo, edad, vision, habilidades, 
        destrezas, formacion, experiencia, cursos, talleres, 
        seminarios, ponencias, publicaciones, becas):

        '''Permite crearle un perfil a un usuario'''

        # None checks        
        email          = email or ""
        sexo           = sexo or ""
        edad           = edad or ""
        vision         = vision or ""
        habilidades    = habilidades or ""
        destrezas      = destrezas or ""
        formacion      = formacion or ""
        experiencia    = experiencia or ""
        cursos         = cursos or ""
        talleres       = talleres or ""
        seminarios     = seminarios or ""
        ponencias      = ponencias or ""
        publicaciones  = publicaciones or ""
        becas          = becas or ""

        u = User()
        findUser = u.getUserByEmail(email)

        findProfile = self.getProfileByEmail(email)
       
        if findProfile == []:

            if findUser != []:
                newProfile = Profile(email,sexo,edad,vision,habilidades,destrezas,
                    formacion,experiencia,cursos,talleres,seminarios,ponencias,
                    publicaciones,becas)
                db.session.add(newProfile)
                db.session.commit()
                return {'status': 'success', 'reason': 'Profile created'}
        else:
            return {'status': 'failure', 'reason': 'Profile already created, Use modify instead'}
        
        return {'status': 'failure', 'reason': 'Couldnt find user  :( '}



    def getProfiles(self):
        '''Permite obtener todos los perfiles'''

        result = self.query.all()
        return result


    def getProfileByEmail(self, email):
        '''Permite buscar un perfil por su correo'''

        profile = self.query.filter_by(email=email).all()
        return profile
    
    def updateProfile(self, email=None, sexo=None, edad=None, vision=None, habilidades=None, 
        destrezas=None, formacion=None, experiencia=None, cursos=None, talleres=None, 
        seminarios=None, ponencias=None, publicaciones=None, becas=None):
        '''Permite actualizar el perfil de un usuario'''

        # None checks
        email          = email or ""
        sexo           = sexo or ""
        edad           = edad or ""
        vision         = vision or ""
        habilidades    = habilidades or ""
        destrezas      = destrezas or ""
        formacion      = formacion or ""
        experiencia    = experiencia or ""
        cursos         = cursos or ""
        talleres       = talleres or ""
        seminarios     = seminarios or ""
        ponencias      = ponencias or ""
        publicaciones  = publicaciones or ""
        becas          = becas or ""

        u = User()
        findUser = u.getUserByEmail(email)

        findProfile = self.getProfileByEmail(email)
        
        if findUser != []:       

            if findProfile != []:

                if sexo != "":
                    findProfile[0].sexo = sexo
                if edad != "":
                    findProfile[0].edad = edad
                if vision != "":
                    findProfile[0].vision = vision
                if habilidades != "":
                    findProfile[0].habilidades = habilidades
                if destrezas != "":
                    findProfile[0].destrezas = destrezas
                if formacion != "":
                    findProfile[0].formacion = formacion
                if experiencia != "":
                    findProfile[0].experiencia = experiencia
                if cursos != "":
                    findProfile[0].cursos = cursos
                if talleres != "":
                    findProfile[0].talleres = talleres
                if seminarios != "":
                    findProfile[0].seminarios = seminarios
                if ponencias != "":
                    findProfile[0].ponencias = ponencias
                if publicaciones !="":
                    findProfile[0].publicaciones = publicaciones
                if becas != "":
                    findProfile[0].becas = becas

                db.session.commit()

                return {'status': 'success', 'reason': 'Profile updated'}

            else:
                return {'status': 'failure', 'reason': 'Profile doesnt exists, Use create instead'}    

        else:

            return {'status': 'failure', 'reason': 'Couldnt find user  :( '}
            
        


    def deleteProfile(self, id):
        ''' permite borrar un perfil de un usuario '''

        findProfile = self.getProfileById(id)

        if findProfile != {'status': 'failure', 'reason': ' Id not integer'}:
            self.query.filter_by(perfilId=id).delete()
            db.session.commit()
            return {'status': 'success', 'reason': 'Profile deleted'}
        else:
            return {'status': 'failure', 'reason': 'Couldnt find Profile :('}

