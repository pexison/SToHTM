stohtModule.service('profileService', ['$http', function($http) {
    this.editProfile = function(args) {
        return  $http({
          url: "user/profile",
          method: 'POST',
          params: args
        });
    };

    this.getProfile = function(args) {
        return  $http({
          url: "user/profile",
          method: 'GET',
          params: args
        });
    };
}]);