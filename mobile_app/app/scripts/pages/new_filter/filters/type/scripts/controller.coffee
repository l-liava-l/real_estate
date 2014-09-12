
App.controller('AreaFilterCtrl', ($scope, core) ->


    type = $scope.type = core.model.filters.itemForEdit.type ?= {
      section: null
      detail: {}
    }

    $scope.list =
      "Квартира":
        {
          "Комната":          false
          "1 комнатная":      false
          "2 комнатная":      false
          "3 комнатная":      false
          "4 комнатная":      false
          "5 комнатная":      false
          "6+ комнатная":     false
        }

      "Дом/Коттедж":
        {
          "Дом":              false
          "Часть дома":       false
          "Таунхаус":         false
        }

      "Нежилое помещение":
        {
          "Офис":             false
          "Торговая площадь": false
          "Склад":            false
          "Своб. назнач.":    false
          "Общепит":          false
          "Гараж":            false
          "Производство":     false
          "Автосервис":       false
          "Здание":           false
          "Бытовые услуги":   false
          "Юр. адрес":        false
          "Участок":          false
        }


    $scope.changeDetailType = (key) ->
      if !type.detail[key]
        delete type.detail[key]
      type.DetailPerv = Object.keys(type.detail)


    $scope.changeType = (name) ->
      if type.section isnt name
        type = $scope.type = core.model.filters.itemForEdit.type = {
          section: null
          detail: {}
        }

      if type.section is "Квартира" || "Дом/Коттедж"
        type.forLive = true
      else
        type.forLive = false

)

