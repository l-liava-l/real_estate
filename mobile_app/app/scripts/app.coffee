'use strict'

App = angular.module('app', [
  'ionic', 'ngResource'
]).run () ->

  App.config [
    '$stateProvider'
    '$urlRouterProvider'
    '$httpProvider'
    ($stateProvider, $urlRouterProvider, $httpProvider) ->

      headers  = $httpProvider.defaults.headers
      headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

      $httpProvider.defaults.transformRequest.unshift (params) ->

        type = params?.type
        data = params?.data

        if type is 'json' then return data
        if angular.isObject(data) then angular.toQueryString(data) else data

      $stateProvider
      #=============  side menu
      .state 'main',
        url: '/main'
        abstract: true
        templateUrl: "templates/pages/side_menu/menu.html"

      #=============  adverts
      .state 'main.advert',
        url: '/advert'
        views:
          menuContent:
            templateUrl: "templates/pages/adverts/new.html"
            controller: "AdvertCtrl"

      .state 'main.bookmarks',
        url: '/bookmarks'
        views:
          menuContent:
            templateUrl: "templates/pages/adverts/bookmarks.html"
            controller: "AdvertCtrl"



      #============== filters

      .state 'main.filters',
        url: '/filters'
        views:
          menuContent:
            templateUrl: "templates/pages/list_filters/list.html"
            controller: "FiltersCtrl"

      .state 'main.add_filter',
        url: '/add-filter'
        views:
          menuContent:
            templateUrl: "templates/pages/new_filter/add-filter.html"
            controller: "AddFilterCtrl"


      .state 'signup',
        url: '/signup'
        abstract: false
        templateUrl: "templates/pages/registration/reg.html"
        controller: "SignupCtrl"



      #================= filters widget pages
      .state 'main.add_filter_type',
        url: '/add-filter/type'
        views:
          menuContent:
            templateUrl: "templates/pages/new_filter/filters/type/page.html"
            controller: "AreaFilterCtrl"

      .state 'main.add_filter_term',
        url: '/add-filter/time'
        views:
          menuContent:
            templateUrl: "templates/pages/new_filter/filters/time/page.html"
            controller: "TermFilterCtrl"

      .state 'main.add_filter_cost',
        url: '/add-filter/cost'
        views:
          menuContent:
            templateUrl: 'templates/pages/new_filter/filters/cost/page.html'
            controller: "CostFilterCtrl"

      .state 'main.add_filter_metro',
        url: '/add-filter/metro'
        views:
          menuContent:
            templateUrl: "templates/pages/new_filter/filters/metro/page.html"
            controller: "MetroFilterCtrl"



      $urlRouterProvider.otherwise "/main/filters"


  ]

