//Controlador del home (usuario)
stohtModule.controller('userController',
   ['$scope', '$location', '$route', 'flash', 'userService', 'loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
        loginService.check({'securityLvl': 2}).then(function (object) {
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];
                } else {
                    $location.path(object.data['redirect']);
                }
            });
        $scope.msg = "";

        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };

    }]);
