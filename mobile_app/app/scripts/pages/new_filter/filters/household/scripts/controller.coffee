App.controller 'HouseholdCtrl', ($scope, core) ->

  ef = $scope.editfilter = core.model.filters.itemForEdit
  ef.household ?= {}


  show = (a) ->
    return a

  $scope.check = (item, id) ->
    if item.checked
      ef.household[id] = item['text']
    else
      delete ef.household[id]



  temp = [
    {
      text: 'Мебель',
      access: () -> show(ef.type?.forLive)
    },
    {
      text: 'Бытовая техника',
      access: () -> show(ef.rent && ef.type?.forLive)
    }
    {
      text: 'Телефон',
      access: () -> show(ef.rent && ef.type?.forLive)
    },
    {
      text: 'Телевизор',
      access: () -> show(ef.rent && ef.type?.forLive)
    },
    {
      text: 'Можно с детьми',
      access: () -> show(ef.rent && ef.type?.forLive)
    },
    {
      text: 'Можно с животными',
      access: () -> show(ef.rent && ef.type?.forLive)
    }
  ]


  $scope.list = () ->
    for id of ef.household
      temp[id]['checked'] = true

    return temp

