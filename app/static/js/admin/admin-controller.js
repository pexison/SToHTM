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



stohtModule.controller('editUserController',
   ['$scope', '$location', '$route', 'flash', 'adminService',
    function ($scope, $location, $route, flash, adminService) {
        $scope.msg = "";
        $scope.formTitle = "Editar Usuario";
        $scope.saveButton = "Actualizar";
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

        $scope.save = function() {
            $location.path('/userList');
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
        $scope.formTitle = "Nuevo Usuario";
        $scope.saveButton = "Crear";
        $scope.users = [{fullName: "Gabriel Russo", email:"globerusso@gmail.com", rol:"Admin" }]
        for (i=0;i<30;i++){
           $scope.users[i]= {id: i, fullName: "Gabriel Russo", email:"globerusso@gmail.com", rol:"Admin" }
        }
        $scope.viewUser = function(id) {
            $location.path('/editUser');
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

        $scope.save = function() {
            $location.path('/userList');
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
