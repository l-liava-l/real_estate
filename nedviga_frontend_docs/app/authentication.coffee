console.log('authentication')

class SessionidView
  url: =>
    url = $('#js-test-cookie-form').data('url')
    sessionid = $('#js-test-cookie-form').find("input[name='sessionid']").val()
    "#{url}?sessionid=#{sessionid}"

  get: (event)=>
    console.log 'get'
    $.get(@url())

  post: (event)=>
    console.log 'post'
    $.post(@url())

  put: (event)=>
    console.log 'put'
    $.put(@url())

  delete: (event)=>
    console.log 'delete'
    $.delete(@url())


sessionid_view = new SessionidView()

$('#js-test-cookie-form').find('.js-get').on('click', sessionid_view.get)
$('#js-test-cookie-form').find('.js-post').on('click', sessionid_view.post)
$('#js-test-cookie-form').find('.js-put').on('click', sessionid_view.put)
$('#js-test-cookie-form').find('.js-delete').on('click', sessionid_view.delete)


#прелогин
$('#js-prelogin-form .js-post').on 'click', (event)->
  event.preventDefault()
  url = $('#js-prelogin-form').data 'url'
  phone = $('#js-prelogin-form').find("input[name='phone']").val()
  data =
    phone: phone
  $.post url, data, (response)=>
    console.log response


#логин

$('#js-login-form .js-post').on 'click', (event)->
  $el = $('#js-login-form')
  url = $el.data('url')
  data =
    phone: $el.find("input[name='phone']").val()
    sms_code: $el.find("input[name='sms_code']").val()
  $.post url, data, (response)=>
    console.log response