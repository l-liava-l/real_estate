App.controller("FiltersCtrl", ($scope, storage, $ionicModal, $location, core) ->


  console.log 'list filters'
  #todo рефракторинг

  if !storage.session.user.key
    $location.path('/signup')

  $scope.ss = core.model

  filters = $scope.ss.filters
  $scope.items = filters.all
  filters.itemForEdit = {}

  remove = (id) ->
    name = filters.all[id].name
    delete filters.advert[name]
    filters.all.splice(id, 1)
    core.save('filters')
    core.sendFilters(null, id)

  edit = (item) ->
    filters.itemForEdit = item
    $location.path('/main/add-filter')

  $scope.selectFilter = (id) ->
    core.model.filters.selected = id
    $location.path('/main/advert')


  createModal = (url, animType) ->
    animType ?= 'slide-in-up'
    $ionicModal.fromTemplateUrl(url, {
      scope: $scope,
      animation: animType
    })

  showModal = (modal, onAgree, param) ->
    modal.then (m)->
      m.show()
      $scope.agree = () ->
        m.hide()
        onAgree(param)
      $scope.cancel = () ->
        m.hide()

  et_modal = createModal('templates/pages/list_filters/modal-windows/edit.html')
  rm_modal = createModal('templates/pages/list_filters/modal-windows/remove.html')

  $scope.remove = (id) ->
    if !$scope.ss.modal
      showModal(rm_modal, remove, id)
    else
      remove(id)


  $scope.edit = (item) ->
    if !$scope.ss.modal
      showModal(et_modal, edit, item)
    else
      edit(item)

  $scope.saveModal = ()->
    core.save('modal')

)
