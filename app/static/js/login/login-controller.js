stohtModule.controller('loginController',
   ['$scope', '$location', '$route', 'flash', 'loginService',
    function ($scope, $location, $route, flash, loginService) {
        $scope.msg = "";

        $scope.authenticate = function() {
            $location.path('/admin');
          //validate login then call a WS for redirect
            /*
            loginService.validar({user: $scope.user, pass: $scope.pass}).then(function (object) {
            if(object.data['error'] != undefined){
              $scope.error = object.data['error'];
            }else{
              $location.path('/login');
            }
          });
           */
      };

    }]);