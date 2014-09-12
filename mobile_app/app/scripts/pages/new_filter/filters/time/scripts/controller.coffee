App.controller('TermFilterCtrl', ($scope, core) ->
#todo refract
	$scope.editfilter = core.model.filters.itemForEdit

	#term filter
	$scope.editfilter['term'] ?= {value: null, text: null}

	$scope.filter_term_list = [
		{ text: "Любой срок", value: 1 },
		{ text: "Посуточно", value: 2 },
		{ text: "От месяца и более", value: 3 },
		{ text: "Несколько месяцев", value: 4 },
		{ text: "Длительный срок", value: 5 }
	]


	$scope.changeTerm = (item) =>
		$scope.editfilter.term.text = item.text

)
