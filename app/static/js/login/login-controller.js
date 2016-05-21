stohtModule.controller('loginController',
   ['$scope', '$location', '$route', 'flash', 'loginService',
    function ($scope, $location, $route, flash, loginService) {
        loginService.check({'securityLvl': 0}).then(function (object) {
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];
                } else {
                    $location.path(object.data['redirect']);
                }
            });
        $scope.msg = "";

        //Iniciar sesion
        $scope.authenticate = function() {

            loginService.authenticate({email: $scope.email, password: $scope.password}).then(function (object) {
            if(object.data['error'] != undefined){
                $scope.msg = object.data['error'];
            }else{
                $scope.rol = object.data['rol'];
                if ($scope.rol == 1){
                    $location.path('/admin');
                }
            }
          });

      };

    }]);



