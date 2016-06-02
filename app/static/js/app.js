// Creación del módulo de la aplicación
var stohtModule = angular.module('eventos', ['ngRoute', 'ngAnimate', 'flash']);
stohtModule.config(function ($routeProvider) {
    $routeProvider.when('/', {
                controller: 'loginController',
                templateUrl: 'views/login/login.html'
            }).when('/signup', {
                controller: 'signupController',
                templateUrl: 'views/signup/signup.html'
            }).when('/admin', {
                controller: 'adminController',
                templateUrl: 'views/home.html'
            }).when('/userList', {
                controller: 'userListController',
                templateUrl: 'views/admin/userList.html'
            }).when('/editUser', {
                controller: 'editUserController',
                templateUrl: 'views/admin/editUser.html'
            }).when('/user', {
                controller: 'userController',
                templateUrl: 'views/home.html'
            }).when('/profile', {
                controller: 'profileController',
                templateUrl: 'views/profile/showProfile.html'
            }).when('/editProfile', {
                controller: 'editProfileController',
                templateUrl: 'views/profile/editProfile.html'
            })
});

stohtModule.controller('stohtController_',  ['$scope', '$http', '$location',
function($scope) {
    $scope.title = "login";
}]);
