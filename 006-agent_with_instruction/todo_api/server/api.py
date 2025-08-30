import os
from typing import cast
from flask import Flask, render_template, request, jsonify
from todo_api.domain.entity.entity import Task
from todo_api.domain.usecase import OperationInteractor

from todo_api.memdb.memdb import MemDB

webroot = os.environ.get("WEBROOT", "./public")

db = MemDB()
op = OperationInteractor(db)

app = Flask(
    __name__,
    static_url_path="",
    static_folder=webroot,
    template_folder=webroot,
)

# index.html
@app.route("/")
def index():
    return render_template("index.html")


# 未完了のタスクの一覧を表示する
# GET /api/tasks
@app.route("/api/tasks", methods=["GET"])
def show_remained_tasks():
    tasks = op.show_tasks()
    return jsonify([serialize_task(task) for task in tasks])


# タスクを登録する
# POST /api/tasks
@app.route("/api/tasks", methods=["POST"])
def append_task():
    task = cast(Task, request.get_json())
    new_task = op.create_task(task)
    return serialize_task(new_task)



# タスクを完了にする
# PATCH /api/tasks/<タスクのID>/done
@app.route("/api/tasks/<int:task_id>/done", methods=["PATCH"])
def done_task(task_id: int):
    task = op.done_task(task_id)
    return serialize_task(task)

from datetime import datetime

def serialize_task(task: Task) -> dict:
    # datetime型をISO8601文字列に変換
    from datetime import datetime as dt
    result = dict(task)
    if "created_at" in result and result["created_at"] is not None:
        if isinstance(result["created_at"], dt):
            result["created_at"] = result["created_at"].isoformat()
    if "completed_at" in result and result["completed_at"] is not None:
        if isinstance(result["completed_at"], dt):
            result["completed_at"] = result["completed_at"].isoformat()
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)