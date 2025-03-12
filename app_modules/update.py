from model import Model
from messages import Message, MakeTask, DeleteTask, EditTask, ChangeTaskStatus
from project_types import Task, AppError, TaskStatus, Priority, Scope
from dataclasses import replace
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Dict, Any


def update(model: Model, msg: Message) -> Model:
    match msg:
        case MakeTask():
            return handle_make_task(model, msg)
        case DeleteTask():
            return handle_delete_task(model, msg)
        case EditTask():
            return handle_edit_task(model, msg)
        case ChangeTaskStatus():
            return handle_change_task_status(model, msg)
        case _:
            return Model(model.task_database, model.task_id_generator, AppError.UNDEFINED_MESSAGE)


def handle_make_task(model: Model, msg: MakeTask) -> Model:
    new_task_id = model.task_id_generator.generate()
    title = msg.title
    attr: Dict[str, Any] = msg.attributes
    task_kwargs: Dict[str, Any] = {
        "title": title,
        "task_id": new_task_id,
        "status": attr.get("status", TaskStatus.TO_DO),
        "priority": attr.get("priority", Priority.NONE),
        "scope": attr.get("scope", Scope.GLOBAL),
        "notes": attr.get("notes", ""),
        "do_date": attr.get("do_date", None),
        "due_date": attr.get("due_date", None),
    }
    new_task = Task(**task_kwargs)
    new_task_database = dict(model.task_database)
    new_task_database[new_task_id] = new_task
    return Model(new_task_database, model.task_id_generator)


def handle_delete_task(model: Model, msg: DeleteTask) -> Model:
    new_task_database = dict(model.task_database)
    task_id = msg.task_id
    if task_id in new_task_database:
        model.task_id_generator.free_task_id(task_id)
        del new_task_database[task_id]
        return Model(new_task_database, model.task_id_generator)
    else:
        return Model(new_task_database, model.task_id_generator, AppError.TASK_ID_NOT_FOUND)


def handle_edit_task(model: Model, msg: EditTask) -> Model:
    new_task_database = dict(model.task_database)
    task_id = msg.task_id
    attr: Dict[str, Any] = msg.attributes
    if task_id in new_task_database:
        task_to_edit = new_task_database[task_id]
        updated_task = _edit_task_attributes(task_to_edit, attr)
        new_task_database[task_id] = updated_task
        return Model(new_task_database, model.task_id_generator)
    else:
        return Model(new_task_database, model.task_id_generator, AppError.TASK_ID_NOT_FOUND)


def handle_change_task_status(model: Model, msg: ChangeTaskStatus) -> Model:
    new_task_database = dict(model.task_database)
    task_id = msg.task_id
    new_task_status = msg.task_status
    if task_id in new_task_database:
        task = new_task_database[task_id]
        if new_task_status == TaskStatus.COMPLETE:
            new_task_database[task_id] = replace(
                task,
                status=new_task_status,
                time_completed=datetime.now().astimezone(ZoneInfo("UTC"))
            )
        else:
            new_task_database[task_id] = replace(
                task,
                status=new_task_status
            )
    return Model(new_task_database, model.task_id_generator)


def _edit_task_attributes(task_to_edit: Task, new_attr: Dict[str, Any]) -> Task:
    return replace(
        task_to_edit,
        title=new_attr.get("title", task_to_edit.title),
        priority=new_attr.get("priority", task_to_edit.priority),
        scope=new_attr.get("scope", task_to_edit.scope),
        notes=new_attr.get("notes", task_to_edit.notes),
        do_date=new_attr.get("do_date", task_to_edit.do_date),
        due_date=new_attr.get("due_date", task_to_edit.due_date)
    )
