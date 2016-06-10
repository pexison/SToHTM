import unittest
from copy import deepcopy
from nose_parameterized import parameterized

from app.models.db import db
from app.models.category import Category

template = dict(
    name="A Category Name",
    isSubCategory=False,
    parentCategory=None,
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

def dup_load():
    result = []
    for i in range(2):
        result += load_test_cases()

    return result

# Placeholder Test case to make a model test file
class TestCategoryModel(unittest.TestCase):
    def setUp(self):
        db.create_all()
        self.Category = Category()

    def tearDown(self):
        db.drop_all()

    # PARAMETERIZED TESTS

    @parameterized.expand(dup_load)
    def test_createCategory(self, _, data):
        categoryCreated = self.Category.createCategory(**data)
        self.assertEqual(categoryCreated['status'], 'success')

    def test_createChildCategory(self):
        data = deepcopy(template)
        self.Category.createCategory(**data)

        category = self.Category.getCategoryByName(data['name'])
        categoryId = category.categoryId

        data2 = deepcopy(template)
        data2['name'] = 'A Subcategory'
        data2['parentCategory'] = categoryId
        subcategoryCreated = self.Category.createCategory(**data2)

        self.assertEqual(subcategoryCreated['status'], 'success')

    def test_createChildCategoryWithoutExistingParent(self):
        data = deepcopy(template)
        data['parentCategory'] = 20
        subcategoryCreated = self.Category.createCategory(**data)

        self.assertNotEqual(subcategoryCreated['status'], 'success')




