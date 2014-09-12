App.controller('RobFilterCtrl', ($scope, core) ->
  ef = $scope.editfilter = core.model.filters.itemForEdit
  ef.rent ?= true
)
