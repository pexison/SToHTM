//Controlador del perfil de usuario
stohtModule.controller('profileController',
   ['$scope', '$location', '$route', 'flash', 'loginService',
    function ($scope, $location, $route, flash, loginService) {

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


        $scope.profile = { email: "person@mnokey.query",
                           gender: "masculino",
                           age: 23,
                           vision: "Ninguna",
                           skills: "Ninguna",
                           experience: "Ninguna",
                           formation: "Ninguna",
                           curses: "Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna ",
                           workshops: "Ninguna",
                           seminars: "Ninguna",
                           papers: "Ninguna",
                           publications: "Ninguna",
                           scholarships: "Ninguna",
                           abilities: "Ninguna"
                         }

        }]);

//Controlador del perfil de usuario
stohtModule.controller('editProfileController',
   ['$scope', '$location', '$route', 'flash', 'loginService',
    function ($scope, $location, $route, flash, loginService) {

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


        $scope.profile = { email: "person@mnokey.query",
                           gender: "masculino",
                           age: 23,
                           vision: "Ninguna",
                           skills: "Ninguna",
                           experience: "Ninguna",
                           formation: "Ninguna",
                           curses: "Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna Ninguna ",
                           workshops: "Ninguna",
                           seminars: "Ninguna",
                           papers: "Ninguna",
                           publications: "Ninguna",
                           scholarships: "Ninguna",
                           abilities: "Ninguna"
                         }

        }]);

