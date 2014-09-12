App.controller('AddFilterCtrl', ($scope, core) ->

  filters = core.model.filters
  $scope.editfilter = filters.itemForEdit

  $scope.save = () ->
    edit = false
    push = () ->
      id = filters.all.length
      if !$scope.editfilter.name
        $scope.editfilter.name = "Фильтр " + (id + 1)
      filters.all.push filters.itemForEdit
      filters.advert[id] = []
      core.sendFilters(filters.itemForEdit)


    if filters.all.length > 0
      for item of filters.all
        if filters.all[item] is filters.itemForEdit
          core.sendFilters(filters.itemForEdit, item)
          edit = true
          break
      if(edit is false)
        push()
    else
      push()

    filters.itemForEdit = {}
    core.save('filters')



)