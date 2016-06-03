// Creación del módulo de la aplicación
var stohtModule = angular.module('eventos', ['ngRoute', 'ngAnimate', 'flash']);
stohtModule.config(function ($routeProvider) {
    $routeProvider.when('/', {
                controller: 'loginController',
                templateUrl: 'views/login/login.html'
            }).when('/signup', {
                controller: 'signupController',
                templateUrl: 'views/login/login.html'
            }).when('/userList', {
                controller: 'userListController',
                templateUrl: 'views/app/editUser.html'
            }).when('/editUser', {
                controller: 'editUserController',
                templateUrl: 'views/app/editUser.html'
            }).when('/home', {
                controller: 'userController',
                templateUrl: 'views/app/home.html'
            }).when('/profile', {
                controller: 'profileController',
                templateUrl: 'views/app/profile.html'
            }).when('/editProfile', {
                controller: 'editProfileController',
                templateUrl: 'views/app/profile.html'
            })
});

stohtModule.controller('stohtController_',  ['$scope', '$http', '$location',
function($scope) {
    $scope.title = "login";
}]);
