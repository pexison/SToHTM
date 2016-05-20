// Creación del módulo de la aplicación
var stohtModule = angular.module('eventos', ['ngRoute', 'ngAnimate', 'flash']);
stohtModule.config(function ($routeProvider) {
    $routeProvider.when('/', {
                controller: 'loginController',
                templateUrl: 'views/login/login.html'
            }).when('/admin', {
                controller: 'adminController',
                templateUrl: 'views/admin/home.html'
            }).when('/userList', {
                controller: 'userListController',
                templateUrl: 'views/admin/userList.html'
            }).when('/editUser', {
                controller: 'editUserController',
                templateUrl: 'views/admin/editUser.html'
            })
});

stohtModule.controller('stohtController_',  ['$scope', '$http', '$location',
function($scope) {
    $scope.title = "login";
}]);
