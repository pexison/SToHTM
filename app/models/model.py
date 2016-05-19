# -*- coding: utf-8 -*-.

# Se importan las librerias necesarias.
import os
from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager

# Conexion con la base de datos.
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'apl.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# Instancia de la aplicacion.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instancia de la base de datos.

db = SQLAlchemy(app)


class classUser (db.Model):
    '''Clase que define el modelo Usuario'''

    __tablename__ = 'user'
    userId = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String(30), unique=True)
    fullname = db.Column(db.String(50))
    password = db.Column(db.String(200))

    def __init__(self, email, fullname, password):
        '''Constructor del modelo usuario'''
        self.email = email
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        '''Representacion en string del modelo Usuario'''
        return \
            '<fullname %r, email %r, username %r >' % (self.userId, self.email,
                                                       self.fullname)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
db.create_all()  # Creamos la base de datos
