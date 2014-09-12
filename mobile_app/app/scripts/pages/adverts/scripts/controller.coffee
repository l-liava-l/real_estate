App.controller 'AdvertCtrl', ($scope, core, $ionicScrollDelegate, $document, $ionicSideMenuDelegate, $compile) ->

  pageName = document.getElementById('advertPage').getAttribute('name')
  delegate = $ionicScrollDelegate.$getByHandle('mainScroll')
  noLoad = false

  $scope.scroll = {can: true}
  $scope.$ionicSideMenuDelegate =  $ionicSideMenuDelegate
  bm = core.model.bookmarks
  $scope.removed = []
  $scope.visible = []
  $scope.advertList = {}


  #todo оптимизировать
  $scope.addToBookmark = (advert) ->
    newName = advert.type + advert.cost
    ->
      advert.bookmark = !advert.bookmark
      if bm.names and bm.names.length
        for name of bm.names
          if bm.names[name] is newName
            bm.data.splice(name, 1)
            bm.names.splice(name, 1)
            exist = true
            break
        if !exist
          bm.data.push(advert)
          bm.names.push(newName)
      else
        bm.names = [newName]
        bm.data = [advert]
      $scope.advertList.react.setState({scope: $scope})
      core.save('bookmarks', bm)


  onMoreLoaded = (data) ->
    if $scope.visible.length >= 20
      elems = angular.element($document[0].querySelectorAll(".card"))
      wasRemoved = true
      height = 0
      for count of elems
        if count <= 10
          height += elems[count].scrollHeight
      extra = $scope.visible.splice(0, 10)
      $scope.removed = $scope.removed.concat(extra)
    if pageName is 'Закладки' then $scope.visible = data['data']
    else
      for item in data['data']
        $scope.visible.push item
    $scope.advertList.react.setState({scope: $scope})
    if wasRemoved
      wasRemoved = false
      delegate.scrollTo(0, height, false)
    $scope.$broadcast('infiniteScrollComplete')

  $scope.loadRemoved = () ->
    backed_adverts = $scope.removed.splice(-10).reverse()
    if backed_adverts.length
      count = 0
      height = 0
      for item in angular.element($document[0].querySelectorAll(".card"))
        count += 1
        if count >= 11
          height += item.scrollHeight
      $scope.visible.splice(-10)
      for item in backed_adverts
        $scope.visible.unshift(item)
      $scope.advertList.react.setState({scope: $scope})
      delegate.scrollTo(0, height, false)
    $scope.$broadcast('infiniteScrollComplete')


  $scope.loadMore = ->
    if !noLoad then core.getAdvert(pageName, onMoreLoaded)
    if pageName is 'Закладки' then noLoad = true


  $scope.$on 'stateChangeSuccess', () -> $scope.loadMore()


  preventSideMenu = ->
    $ionicSideMenuDelegate.canDragContent(false)

  startSideMenu = ->
    $ionicSideMenuDelegate.canDragContent(true)


  onswipe = (event) ->
    slidebox = event.target
    direction = event.gesture.direction


    if direction is 'left'
      changeSlide(slidebox.children[0], 1)
    else if direction is 'right'
      changeSlide(slidebox.children[0], -1)


  changeSlide = (slideElem, num) ->
    console.log slideElem.currentSlide, slideElem.slidePos,slideElem.slidePos[slideElem.currentSlide + num]
    slideElem.style.left = -slideElem.slidePos[slideElem.currentSlide + num]  + 'px'

    if slideElem.slidePos[slideElem.currentSlide + num]
      slideElem.currentSlide += num



  $scope.$watchCollection 'visible', ->
    for elem in document.getElementsByClassName("slidebox")


      slideWrap =  elem.children[0].slidePos ?= []
      slideWidth = elem.offsetWidth


      elem.children[0].currentSlide ?= 0

      ionic.onGesture('dragstart', preventSideMenu, elem)
      ionic.onGesture('dragend', startSideMenu, elem)
      ionic.onGesture('swipe', onswipe, elem)


      for i of elem.children[0].children
        slide = parseInt(i)
        if slide isnt slide then break

        newPos = slideWidth * slide

        match = false
        for pos in slideWrap
          if pos is newPos then match = true

        if !match then  slideWrap.push(newPos)











