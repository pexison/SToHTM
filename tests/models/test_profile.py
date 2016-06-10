import unittest
from copy import deepcopy
from nose_parameterized import parameterized

from app.models.db import db
from app.models.user import User
from app.models.profile import Profile

template = dict(
    email="manuelalejandropm@gmail.com",
    gender="Masculino",
    age=22,
    vision="Alguna Vision",
    abilities="Algunas habilidades",
    skills="Algunas destrezas",
    formation="Algunas formacion",
    experience="Alguna experiencia",
    courses="Algunso cursos",
    workshops="Algunos talleres",
    seminars="Algunso seminarions",
    papers="Algunas ponencias",
    publications="Algunas publicaciones",
    scholarships="Algunas becas",
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
