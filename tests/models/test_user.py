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
        userCreated = self.User.createUser("manuelalejandropm@gmail.com", "Manuel Pacheco", "somepassword")
        self.assertEqual(userCreated['status'], 'success');


if __name__ == '__main__':
    unittest.main()
