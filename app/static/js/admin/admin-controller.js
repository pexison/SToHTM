stohtModule.controller('adminController',
   ['$scope', '$location', '$route', 'flash', 'adminService',
    function ($scope, $location, $route, flash, adminService) {
        $scope.msg = "";
        $scope.logout = function() {
            $location.path('/');
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



stohtModule.controller('userListController',
   ['$scope', '$location', '$route', 'flash', 'adminService',
    function ($scope, $location, $route, flash, adminService) {
        $scope.msg = "";
        $scope.logout = function() {
            $location.path('/');
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