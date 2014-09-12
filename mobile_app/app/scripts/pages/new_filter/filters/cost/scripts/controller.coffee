App.controller 'CostFilterCtrl', ($scope, core) ->
  $scope.cost = core.model.filters.itemForEdit.cost ?= {}
