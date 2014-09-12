App.factory 'storage',() ->
  s =
    session: angular.copy window.localStorage

  s.saveToLocal = (prop, val) ->

    if !prop
      forSave = this.session

    if prop && !val
      forSave = this.session[prop]

    if prop && val
      forSave = this.session[prop] = val

    window.localStorage.setItem(prop,
      JSON.stringify(
        angular.copy forSave
      )
    )

  s.loadFromLocal = (prop) ->
    if typeof this.session[prop] is 'object'
      if window.localStorage.getItem(prop)
        this.session[prop] = JSON.parse window.localStorage.getItem(prop)


  for item of s.session
    try
      s.session[item] = JSON.parse s.session[item]


  return s




