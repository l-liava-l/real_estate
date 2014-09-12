App.factory 'planner', ['storage', (storage) ->
  {
    $tasks: []

    add: (func) ->
      if !func then return

      getArg = (arg)->
        output = []
        for i of arg
          if parseInt(i) > 1
            output.push(arg[i])
        return output

      task =
        func:  func + ''
        arg: getArg(arguments)


      this.$tasks.push(task)

      console.log this.$tasks
      storage.saveToLocal('$tasks', [])

    exe: () ->
      for task in this.$tasks
        task.func.apply(this, task.arg)
  }
]