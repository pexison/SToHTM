//Controlador del home (administrador)
stohtModule.controller('adminController',
   ['$scope', '$location', '$route', 'flash', 'adminService', 'loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
        loginService.check({'securityLvl': 1}).then(function (object) {
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

//controlador de edicion de usuario (administrador)
stohtModule.controller('editUserController',
   ['$scope', '$location', '$route', 'flash', 'adminService','loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
        loginService.check({'securityLvl': 1}).then(function (object) {
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];
                } else {
                    $location.path(object.data['redirect']);
                }
            });
        $scope.msg = "";
        $scope.changeMail = "checked";
        $scope.formTitle = "Editar Usuario";
        $scope.saveButton = "Actualizar";

        $scope.id=$location.search()['user'];
        $scope.roles=[{name:"Administrador", value:1},{name:"Usuario",value:2}];

        //Obtener datos de usuario
        adminService.getUser({id: $scope.id}).then(function (object) {
            if(object.data['error'] != undefined){
              $scope.error = object.data['error'];
            }else{

                $scope.id=object.data['id'];
                $scope.email=object.data['email'];
                $scope.password="";
                $scope.passwordr="";
                $scope.fullName=object.data['fullName'];
                $scope.chosenRole=$scope.roles[(object.data['rol'])-1];
            }
          });


        //Guardar cambios
        $scope.save = function() {
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


        //cierre de sesion
        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };

    }]);

//controlador de creacion de usuarios y lista de usuarios (administrador)
stohtModule.controller('userListController',
   ['$scope', '$location', '$route', 'flash', 'adminService','loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
        loginService.check({'securityLvl': 1}).then(function (object) {
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];
                } else {
                    $location.path(object.data['redirect']);
                }
            });
        $scope.msg = "";
        $scope.changeMail = "";
        $scope.formTitle = "Nuevo Usuario";
        $scope.saveButton = "Crear";

        $location.search({});
        $scope.roles=[{name:"Administrador", value:1},{name:"Usuario",value:2}];
        $scope.chosenRole=$scope.roles[1];

        //Ver usuario
        $scope.viewUser = function(id) {
            $location.search('user', id);
            $location.path('/editUser');
        };

        //Obtener Lista de usuarios
        adminService.users({}).then(function (object) {
            if(object.data['result'] != undefined){
              $scope.users = object.data['result'];
            }else{
                $scope.users = [];
            }
          });

        //Crear usuario
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

        //Eliminar usuario
        $scope.delete = function(id) {
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

                    //Recargar lista de usuarios
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

        //cierre de sesion
        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };
    }]);
