stohtModule.controller('adminController',
   ['$scope', '$location', '$route', 'flash', 'adminService',
    function ($scope, $location, $route, flash, adminService) {
        $scope.msg = "";
        $scope.logout = function() {
            $location.path('/');
      };

    }]);



stohtModule.controller('editUserController',
   ['$scope', '$location', '$route', 'flash', 'adminService',
    function ($scope, $location, $route, flash, adminService) {
        $scope.msg = "";
        $scope.formTitle = "Editar Usuario";
        $scope.saveButton = "Actualizar";
        var searchObject = $location.search();
        $scope.id=searchObject['user'];
        alert($scope.id);


        adminService.getUser({id: $scope.id}).then(function (object) {
            if(object.data['error'] != undefined){
              $scope.error = object.data['error'];
            }else{
                $scope.roles=[{name:"Administrador", value:1},{name:"Usuario",value:2}];
                $scope.id=object.data['id'];
                $scope.email=object.data['email'];
                $scope.password="";
                $scope.passwordr="";
                $scope.fullName=object.data['fullName'];
                $scope.chosenRole=$scope.roles[(object.data['rol'])-1];
            }
          });


        $scope.logout = function() {
            $location.path('/');
      };

        $scope.save = function() {
          //validate login then call a WS for redirect
            if ($scope.password == $scope.passwordr) {
                adminService.updateUser({
                    email: $scope.email,
                    password: $scope.password,
                    rol: $scope.chosenRole.value,
                    fullName: $scope.fullName
                }).then(function (object) {
                    if (object.data['error'] != undefined) {
                        $scope.msg = object.data['error'];
                    } else {
                        $location.path('/userList');
                    }
                });
            }else{
                $scope.msg="Las contraseñas no coinciden";
            }

      };

    }]);

stohtModule.controller('userListController',
   ['$scope', '$location', '$route', 'flash', 'adminService',
    function ($scope, $location, $route, flash, adminService) {
        $location.search({});
        $scope.viewUser = function(id) {
            $location.search('user', id);
            $location.path('/editUser');

      };
        adminService.users({}).then(function (object) {
            if(object.data['result'] != undefined){
              $scope.users = object.data['result'];
            }else{
                $scope.users = [];
            }
          });


        $scope.save = function() {
          //validate login then call a WS for redirect
            if ($scope.password == $scope.passwordr){
                adminService.createUser({email: $scope.email, password: $scope.password, rol:$scope.chosenRole.value, fullName: $scope.fullName}).then(function (object) {
                if(object.data['error'] != undefined){
                  $scope.msg = object.data['error'];
                }else{
                    $scope.email="";
                    $scope.password="";
                    $scope.passwordr="";
                    $scope.fullName="";
                    $scope.msg = "";
                  $scope.msg = object.data['reason'];
                    adminService.users({}).then(function (object) {
                    if(object.data['result'] != undefined){
                      $scope.users = object.data['result'];
                    }else{
                        $scope.users = [];
                    }
                  });
                  $location.path('/userList');
                }
              });
            }else{
                $scope.msg="Las contraseñas no coinciden";
            }

      };

        $scope.delete = function(id) {
          //validate login then call a WS for redirect
                adminService.deleteUser({userId: id}).then(function (object) {
                if(object.data['error'] != undefined){
                  $scope.msg = object.data['error'];
                }else{
                    $scope.email="";
                    $scope.password="";
                    $scope.passwordr="";
                    $scope.fullName="";
                    $scope.msg = "";
                  $scope.msg = object.data['reason'];
                    adminService.users({}).then(function (object) {
                    if(object.data['result'] != undefined){
                      $scope.users = object.data['result'];
                    }else{
                        $scope.users = [];
                    }
                  });
                  $location.path('/userList');
                }
              });

      };

        $scope.logout = function() {
            $location.path('/');
      };

        $scope.formTitle = "Nuevo Usuario";
        $scope.saveButton = "Crear";

        $scope.roles=[{name:"Administrador", value:1},{name:"Usuario",value:2}];
        $scope.chosenRole=$scope.roles[1];

    }]);
