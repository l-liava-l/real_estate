console.log 'adverts'


$('#js-random-adverts .js-get').on 'click', (event)->
  $el = $('#js-random-adverts')
  url = $el.data 'url'
  data =
    page: $el.find("input[name='page']").val()
  $.get url, data, (response)=>
    console.log response


$('#js-adverts-by-filter .js-get').on 'click', (event)->
  $el = $('#js-adverts-by-filter')
  url = $el.data 'url'
  data =
    filter_id: $el.find("input[name='filter_id']").val()
  $.get url, data, (response)=>
    console.log response