//controlador de creacion de usuarios y lista de usuarios (administrador)
stohtModule.controller('categoriesController',
   ['$scope', '$location', '$route', 'flash', 'categoryService','loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
        $scope.view= "categories";

        loginService.check({'securityLvl': 16}).then(function (object) {
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];

                    $scope.isAdmin= ($scope.actorRol & 1) !== 0;
                    $scope.isOperator= ($scope.actorRol & 2) !== 0;
                    $scope.isClient = ($scope.actorRol & 4) !==0;
                    $scope.isManager = ($scope.actorRol & 16) !==0;
                } else {
                    $location.path(object.data['redirect']);
                }
            });
        $scope.msg = "";
        $scope.category= {name: "Ejemplo 1"};
        $scope.categories=[{name:"Subejemplo1",id:1},{name:"Subejemplo2",id:2},{name:"Subejemplo3",id:3}];
        $scope.crumbs=[{name:"crumb1", id: 1},{name:"crumb2", id: 1},{name:"crumb3", id: 1}];
        $scope.supercategories=[{name:"super categoria 1",id:1},{name:"super categoria 2",id:2},{name:"super categoria 3",id:3}];
        $location.search({});

        //Ver categoria
        $scope.viewCategory = function(id) {
            //servicio para ver categoria
        };

        //Obtener Lista de categorias
        /*
        categoryService.categories({}).then(function (object) {
            if(object.data['result'] != undefined){
              $scope.categories = object.data['result'];
            }else{
                $scope.categories = [];
            }
          });
        */

        //Crear categoria
        $scope.save = function() {
                /*
                categoryService.createCategory({nombre: $scope.name}).then(function (object) {
                if (object.data['error'] != undefined) {
                        $scope.msg = object.data['error'];
                    } else {
                        if (object.data['status'] != 'failure') {
                            $scope.msg = object.data['reason'];
                            categoryService.categories({}).then(function (object) {
                                if(object.data['result'] != undefined){
                                  $scope.categories = object.data['result'];
                                }else{
                                    $scope.categories = [];
                                }
                              });
                        }else{
                            $scope.msg = object.data['reason'];
                        }
                    }
              });
        */

      };

        //Eliminar categoria
        $scope.delete = function(id) {
            /*
                categoryService.deleteCategory({userId: id}).then(function (object) {
                if(object.data['error'] != undefined){
                  $scope.msg = object.data['error'];
                }else{
                    $scope.msg = object.data['reason'];

                    //Recargar lista de categorias
                    categoryService.categories({}).then(function (object) {
                        if(object.data['result'] != undefined){
                          $scope.categories = object.data['result'];
                        }else{
                            $scope.categories = [];
                        }
                      });

                }
              });
              */

      };

        //cierre de sesion
        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };
    }]);
