import unittest
from copy import deepcopy
from nose_parameterized import parameterized

from app.models.db import db
from app.models.user import User
from app.models.profile import Profile

template = dict(
    email="manuelalejandropm@gmail.com",
    sexo="Masculino",
    edad=22,
    vision="Alguna Vision",
    habilidades="Algunas habilidades",
    destrezas="Algunas destrezas",
    formacion="Algunas formacion",
    experiencia="Alguna experiencia",
    cursos="Algunso cursos",
    talleres="Algunos talleres",
    seminarios="Algunso seminarions",
    ponencias="Algunas ponencias",
    publicaciones="Algunas publicaciones",
    becas="Algunas becas",
)

def load_test_cases():
    result = []

    for key in iter(template):

        # Test None
        data = deepcopy(template)
        data[key] = None
        result.append(("Without" + key.capitalize(), data))

        # Test Empty
        data = deepcopy(template)
        data[key] = ""
        result.append(("WithEmpty" + key.capitalize(), data))

    return result

# Placeholder Test case to make a model test file
class TestProfileModel(unittest.TestCase):
    def setUp(self):
        db.create_all()
        self.User = User().createUser("manuelalejandropm@gmail.com", "Manuel Pacheco", "somepassword", 1)
        self.Profile = Profile()

    def tearDown(self):
        db.drop_all()

    # PARAMETERIZED TESTS

    @parameterized.expand(load_test_cases)
    def test_createProfile(self, _, data):
        profileCreated = self.Profile.createProfile(**data)
        self.assertEqual(profileCreated['status'], 'success')

    # CORE TESTS

    def test_createCommonProfile(self):
        data = deepcopy(template)

        profileCreated = self.Profile.createProfile(**data)
        self.assertEqual(profileCreated['status'], 'success')

    # EMAIL TESTS

    def test_createProfileWithoutEmail(self):
        data = deepcopy(template)
        data['email'] = None

        profileCreated = self.Profile.createProfile(**data)
        self.assertEqual(profileCreated['status'], 'success')  # TODO SHOULD FAIL

    def test_createProfileWithEmptyEmail(self):
        data = deepcopy(template)
        data['email'] = ""

        profileCreated = self.Profile.createProfile(**data)
        self.assertEqual(profileCreated['status'], 'success')  # TODO SHOULD FAIL

    def test_createProfileWithoutSex(self):
        data = deepcopy(template)
        data['sexo'] = None

        profileCreated = self.Profile.createProfile(**data)
        self.assertEqual(profileCreated['status'], 'success')

    def test_createUserWithEmptySex(self):
        data = deepcopy(template)
        data['sexo'] = ""

        profileCreated = self.Profile.createProfile(**data)
        self.assertEqual(profileCreated['status'], 'success')

