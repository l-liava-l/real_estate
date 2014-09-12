App.factory 'server', ['$resource', ($resource) ->


  ###
  sock = new SockJS(' http://192.168.0.106:8000')

  sock.onopen = () ->

  sock.onmessage = (e) ->

  sock.onclose = () ->
  ###

  api = (url, headers) ->
    $resource('http://94.159.40.122:9000' + url, {

    }, {
      #$resource('http://127.0.0.1:8000' + url, {}, {
      get:
        method: 'GET'
      post:
        method: 'POST'
        headers: headers
    }, {
      stripTrailingSlashes: false
    })

  return api
]

