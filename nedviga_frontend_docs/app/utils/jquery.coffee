jQuery.each [
  "put"
  "delete"
], (i, method) ->
  jQuery[method] = (url, data, callback, type) ->
    if jQuery.isFunction(data)
      type = type or callback
      callback = data
      data = undefined
    jQuery.ajax
      url: url
      type: method
      dataType: type
      data: data
      success: callback
