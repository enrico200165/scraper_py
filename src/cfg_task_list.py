

class CfgTaskList():
    
    def __init__(self, id):
        self._id = id
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    
    def __str__(self):
        ret = []
        for t in self._tasks:
            ret.append(str(t))

        return ",".join(ret)
    
