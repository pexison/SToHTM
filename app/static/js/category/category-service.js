stohtModule.service('categoryService', ['$q', '$http', function($q, $http) {
    this.createCategory = function(args) {
        return  $http({
          url: "category/create",
          method: 'POST',
          params: args
        });
    };

    this.deleteCategory = function(args) {
        return  $http({
          url: "category/delete",
          method: 'POST',
          params: args
        });
    };

    this.updateCategory = function(args) {
        return  $http({
          url: "category/update",
          method: 'PUT',
          params: args
        });
    };

    this.categories = function(args) {
        return  $http({
          url: "categories",
          method: 'GET',
          params: args
        });
    };

    this.getCategoriey = function(args) {
        return  $http({
          url: "category",
          method: 'GET',
          params: args
        });
    };

}]);


