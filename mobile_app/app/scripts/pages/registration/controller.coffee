App.controller 'SignupCtrl',  ($scope, core, auth, $location, $document)->


  $scope.user = core.model.user ?= {
    phone: null
    key: null
  }

  onprelogin = (data) ->
    if data['success']
      $scope.pre = true
      $scope.phoneisnotvalid = false
    else
      $scope.phoneisnotvalid = true



  onlogin = (data) ->
    if data['success']
      core.model.user.sessionid = data.data['sessionid']
      core.save('user', null, false)
      $location.path('default')



  $scope.sendPhone = (valid) ->
    if valid
      auth.prelogin('7' + $scope.user.phone, onprelogin)

      
  $scope.checkPhone = (valid) ->
    if valid
      auth.login('7' + $scope.user.phone, $scope.user.key, onlogin)

  $scope.editPhone = () ->
    $scope.pre = false
