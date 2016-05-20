import unittest

from app.models.db import db
from app.models.user import User


# Placeholder Test case to make a model test file
class TestUserModel(unittest.TestCase):
    def setUp(self):
        db.create_all()
        self.User = User()

    def tearDown(self):
        db.drop_all()

    def test_createCommonUser(self):
        userCreated = self.User.createUser("manuelalejandropm@gmail.com", "Manuel Pacheco", "somepassword", 1)
        self.assertEqual(userCreated['status'], 'success')

    def test_createUserWithoutEmail(self):
        userCreated = self.User.createUser(None, "Manuel Pacheco", "somepassword", 1)
        self.assertEqual(userCreated['status'], 'failure')

    def test_createUserWithEmptyEmail(self):
        userCreated = self.User.createUser("", "Manuel Pacheco", "somepassword", 1)
        self.assertEqual(userCreated['status'], 'failure')

    def test_createUserWithoutName(self):
        userCreated = self.User.createUser("manuelalejandropm@gmail.com", None, "somepassword", 1)
        self.assertEqual(userCreated['status'], 'failure')

    def test_createUserWithEmptyName(self):
        userCreated = self.User.createUser("manuelalejandropm@gmail.com", "", "somepassword", 1)
        self.assertEqual(userCreated['status'], 'failure')

    def test_createUserWithoutPassword(self):
        userCreated = self.User.createUser("manuelalejandropm@gmail.com", "Manuel Pacheco", None, 1)
        self.assertEqual(userCreated['status'], 'failure')

    def test_createUserWithEmptyPassword(self):
        userCreated = self.User.createUser("manuelalejandropm@gmail.com", "Manuel Pacheco", "", 1)
        self.assertEqual(userCreated['status'], 'failure')


if __name__ == '__main__':
    unittest.main()
