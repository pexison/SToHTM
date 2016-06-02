//Controlador del perfil de usuario
stohtModule.controller('profileController',
   ['$scope', '$location', '$route', 'flash', 'loginService', 'profileService',
    function ($scope, $location, $route, flash, loginService, profileService) {

      loginService.check({'securityLvl': 2}).then(function (object) {
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];
                    $scope.actorId = object.data['actorId'];
                } else {
                    $location.path(object.data['redirect']);
                }
            });

        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };

        // TODO: Uncomment
        //$scope.profile = profileService.getProfile($scope.actorId);

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
   ['$scope', '$location', '$route', 'flash', 'loginService', 'profileService',
    function ($scope, $location, $route, flash, loginService, profileService) {

      loginService.check({'securityLvl': 2}).then(function (object) {
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];
                    $scope.actorId = object.data['actorId'];
                } else {
                    $location.path(object.data['redirect']);
                }
            });

        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };

        // TODO: Uncomment
        //$scope.profile = profileService.getProfile($scope.actorId);

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

        $scope.sendForm = function() {
          // TODO send $scope.profile
          // TODO: Uncomment
          //profileService.editProfile($scope.profile);
        }

        }]);

