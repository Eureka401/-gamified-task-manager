from dataclasses import dataclass, field
from typing import Dict, Any
from project_types import TaskStatus


class Message:
    pass


@dataclass(frozen=True)
class MakeTask(Message):
    title: str
    attributes: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DeleteTask(Message):
    task_id: int


@dataclass(frozen=True)
class EditTask(Message):
    task_id: int
    attributes: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ChangeTaskStatus(Message):
    task_id: int
    task_status: TaskStatus
