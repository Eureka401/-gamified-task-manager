from dataclasses import dataclass, field
from enum import Enum, auto
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Optional, TypeAlias


class TaskStatus(Enum):
    COMPLETE = auto()
    WONT_DO = auto()
    TO_DO = auto()


class Priority(Enum):
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()
    NONE = auto()


class Scope(Enum):
    GLOBAL = auto()
    SELECTED = auto()
    LOCAL = auto()


class AppError(Enum):
    TASK_ID_NOT_FOUND = auto()
    UNDEFINED_MESSAGE = auto()


@dataclass(frozen=True)
class Task:
    title: str
    task_id: int
    status: TaskStatus
    priority: Priority
    scope: Scope
    notes: str
    do_date: Optional[datetime] = field(default=None)
    due_date: Optional[datetime] = field(default=None)
    time_completed: Optional[datetime] = field(default=None)
    time_created: datetime = field(
        default_factory=lambda: datetime.now().astimezone(ZoneInfo("UTC")))


TaskDatabase: TypeAlias = dict[int, Task]
