from model import Model
from messages import Message, MakeTask, DeleteTask, EditTask
from project_types import Task, AppError, TaskStatus, Priority, Scope
from dataclasses import replace
from typing import Dict, Any


def update(model: Model, msg: Message) -> Model:
    match msg:
        case MakeTask():
            new_task_id = model.task_id_generator.generate()
            title = msg.title
            attr = msg.attributes

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
        case DeleteTask():
            new_task_database = dict(model.task_database)
            task_id = msg.task_id
            if task_id in new_task_database:
                model.task_id_generator.free_task_id(task_id)
                del new_task_database[task_id]
                return Model(new_task_database, model.task_id_generator)
            else:
                return Model(new_task_database, model.task_id_generator, AppError.TASK_ID_NOT_FOUND)
        case EditTask():
            new_task_database = dict(model.task_database)
            task_id = msg.task_id
            attr = msg.attributes
            if task_id in new_task_database:
                task_to_edit = new_task_database[task_id]
                updated_task = _edit_task_attributes(task_to_edit, attr)
                new_task_database[task_id] = updated_task
                return Model(new_task_database, model.task_id_generator)
            else:
                return Model(new_task_database, model.task_id_generator, AppError.TASK_ID_NOT_FOUND)
        case _:
            return Model(model.task_database, model.task_id_generator, AppError.UNDEFINED_MESSAGE)


def _edit_task_attributes(task_to_edit: Task, new_attr: Dict[str, Any]) -> Task:
    return replace(
        task_to_edit,
        title=new_attr.get("title", task_to_edit.title),
        status=new_attr.get("status", task_to_edit.status),
        priority=new_attr.get("priority", task_to_edit.priority),
        scope=new_attr.get("scope", task_to_edit.scope),
        notes=new_attr.get("notes", task_to_edit.notes),
        do_date=new_attr.get("do_date", task_to_edit.do_date),
        due_date=new_attr.get("due_date", task_to_edit.due_date)
    )
