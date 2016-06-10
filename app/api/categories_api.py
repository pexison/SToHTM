from flask import Blueprint, json, request

from app.models.category import Category

category = Blueprint('category', __name__,)


@category.route('/categories/create', methods=['POST'])
def create_category():
    name = request.args.get('name')
    isSubcategory = request.args.get('isSubCategory') or None
    parentCategory = request.args.get('parentCategory') or None
    if request.args.get('name') is None or len(request.args.get('name')) == 0:
        res = {'error': 'You must provide a valid category name.'}
    else:
        CategoryInstance = Category()
        result = CategoryInstance.createCategory(
            name, isSubcategory, parentCategory)
        res = result

    return json.dumps(res)


@category.route('/categories', methods=['GET'])
def get_categories():
    CategoryInstance = Category()
    result = CategoryInstance.getCategories()
    res = result

    return json.dumps(res)


@category.route('/category', methods=['GET'])
def get_category():
    name = request.args.get('name')
    if request.args.get('name') is None or len(request.args.get('name')) == 0:
        res = {'error': 'You must provide a valid category name.'}
    else:
        CategoryInstance = Category()
        result = CategoryInstance.getCategoryByName(name)
        res = result

    return json.dumps(res)


@category.route('/categories/delete', methods=['POST'])
def delete_category():
    id = request.args.get('id')
    if request.args.get('id') is None or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid category id.'}
    else:
        CategoryInstance = Category()
        result = CategoryInstance.deleteCategory(id)
        res = result

    return json.dumps(res)


@category.route('/categories/update', methods=['POST'])
def update_category():
    id = request.args.get('id')
    name = request.args.get('name') or None
    isSubcategory = request.args.get('isSubcategory') or None
    parentCategory = request.args.get('parentCategory') or None
    if request.args.get('id') is None or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid category id.'}
    else:
        CategoryInstance = Category()
        result = CategoryInstance.updateCategory(
            id, name, isSubcategory, parentCategory)
        res = result

    return json.dumps(res)
