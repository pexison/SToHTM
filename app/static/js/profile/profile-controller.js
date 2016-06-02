//Controlador del perfil de usuario
stohtModule.controller('profileController', 
   ['$scope', '$location', '$route', 'flash',
    function ($scope, $location, $route, flash) {
        $scope.profile = { email: "person@mnokey.query",
                           gender: "masculino",
                           age: 23,
                           vision: "Ninguna",
                           skills: "Ninguna",
                           experience: "Ninguna",
                           formation: "Ninguna",
                           curses: "Ninguna",
                           workshops: "Ninguna",
                           seminars: "Ninguna",
                           papers: "Ninguna",
                           publications: "Ninguna",
                           scholarships: "Ninguna",
                           abilities: "Ninguna"
                         }

        }]);

