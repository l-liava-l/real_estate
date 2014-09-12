App.factory 'core', [
  'storage'
  'server'
  'planner'
  '$cordovaNetwork'
  (storage, server, planner, $cordovaNetwork) ->

    storage.session.bookmarks ?= {data: [], names: []}
    storage.session.user ?=  {}
    storage.session.modal ?= false
    storage.session.filters ?= {
      itemForEdit: {}
      advert: {}
      all: []
    }

    planner.$tasks = storage.session.$tasks ?= []


    return {
      model: storage.session

      save  : (key, value, sync) ->
        storage.saveToLocal(key, value)

      sendFilters: (filter, id) ->
        send = (filter, id) ->
          server('/api/filters/save/', {"Content-Type": "application/json charset=UTF-8"}).post({
            data: {
              filter: JSON.stringify(angular.copy filter)
              id: id
              sessionid: storage.session.user.sessionid
            }
            type: 'json'
          })

        planner.add(send, filter, id)



      getAdvert: (page, onSuccess) ->
        if page is 'Закладки' then onSuccess(storage.session.bookmarks)#
        else if page is 'Объявления' then server('/api/adverts/random/').get(onSuccess)

    }
]
