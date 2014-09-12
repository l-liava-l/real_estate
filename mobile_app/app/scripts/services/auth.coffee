App.factory 'auth', ['server',  (server) ->


  path = '/api/authentication/'

  return {
    prelogin: (phone, callback) ->
      server(path + 'prelogin/').post({
        data: {
          phone: phone
        }
      }, callback)

    login: (phone, key, callback) ->
      server(path + 'login/').post({
        data: {
          phone: phone
          key: key
        }
      }, callback)
  }


]
