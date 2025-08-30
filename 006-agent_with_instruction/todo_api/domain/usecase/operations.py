
from todo_api.domain.entity.entity import Task
from todo_api.memdb.memdb import MemDB
from datetime import datetime


class OperationInteractor:
    def __init__(self, memdb: MemDB):
        self._db = memdb

    def show_tasks(self) -> list[Task]:
        return self._db.search_unfinished()

    def create_task(self, task: Task) -> Task:
        task["done"] = False
        if "created_at" not in task or task["created_at"] is None:
            task["created_at"] = datetime.now()
        task["completed_at"] = None
        self._db.add(task)
        return task

    def done_task(self, task_id: int)-> Task:
        task = self._db.get(task_id)
        if task is None:
            raise Exception("not found")
        task["done"] = True
        if "completed_at" not in task or task["completed_at"] is None:
            task["completed_at"] = datetime.now()
        self._db.update(task)
        return task
