stohtModule.service('loginService', ['$q', '$http', function($q, $http) {

this.authenticate = function(args) {
        return  $http({
          url: "user/authenticate",
          method: 'POST',
          params: args
        });
    };

    /*
   this.checkActor = function(args){
        return  $http({
          url: "normal/checkActor",
          method: 'GET',
          params: args
        });
   };



    this.registrarUsuario = function(args) {
        return  $http({
          url: "normal/register",
          method: 'POST',
          params: args
        });
    };

    this.logout = function(args) {
        return  $http({
          url: "normal/logout",
          method: 'POST',
          params: args
        });
    };
*/
}]);
