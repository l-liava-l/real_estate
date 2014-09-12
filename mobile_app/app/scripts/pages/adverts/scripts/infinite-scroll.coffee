App.directive 'infiniteScroll', ($document, $timeout, $ionicScrollDelegate) ->
  is_loading = false
  delegate = $ionicScrollDelegate.$getByHandle('mainScroll')

  link: (scope, element, attrs) ->
    raw = element[0]

    element.bind 'scroll', ->
      count = 0
      height = 0
      position = delegate.getScrollPosition()
      maxValues = delegate.getScrollView().getScrollMax()
      if position.top <= 0 and not is_loading
        is_loading = true
        scope.loadRemoved()
      if position.top >= maxValues.top and not is_loading
        is_loading = true
        scope.loadMore()

    scope.$on 'infiniteScrollComplete', () =>
      $timeout( () =>
          delegate.getScrollView().resize()
          is_loading = false
        , 0, false)




App.directive 'ngReactComponent', ($timeout) ->
  link: (scope, element, attrs) ->
    raw = element[0]
    renderComponent = () =>
      React.renderComponent(
        window[attrs.ngReactComponent]({ scope: scope }), raw)

    $timeout () =>
      renderComponent()
