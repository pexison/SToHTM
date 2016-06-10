from flask import Blueprint, json, request, session

from app.models.category import Category

category = Blueprint('category', __name__,)


@category.route('/category/children', methods=['GET'])
def get_category_children():
    category = request.args.get('category')
    if category is None or len(category) == 0:
        result = {'error': 'Debe proporcionar una categoría válida.'}
    else:
        CategoryInstance = Category()
        category = CategoryInstance.getCategoryByName(category)

        if not category:
            result = {'error': 'La categoría no existe.'}

        else:
            result = CategoryInstance.getSubCategories(category.categoryId)
            print(result)
            result = list(map(lambda category: {'id': category.categoryId,
                    'name': category.name,
                    'isSubCategory': category.isSubCategory,
                    'parentCategory': category.parentCategory}, result))


    return json.dumps(result)


@category.route('/category/path', methods=['GET'])
def get_category_path():
    category = request.args.get('category')
    if category is None or len(category) == 0:
        result = {'error': 'Debe proporcionar una categoría válida.'}
    else:
        CategoryInstance = Category()
        category = CategoryInstance.getCategoryByName(category)

        if not category:
            result = {'error': 'La categoría no existe.'}

        else:
            result = []

            while category.parentCategory:
                category = CategoryInstance.getCategoryById(category.parentCategory)
                result.append({'id': category.categoryId,
                    'name': category.name,
                    'isSubCategory': category.isSubCategory,
                    'parentCategory': category.parentCategory})

    return json.dumps(result)
