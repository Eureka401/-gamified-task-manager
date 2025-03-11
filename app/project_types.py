from dataclasses import dataclass, field
from enum import Enum, auto
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Optional


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


type Task_DB = dict[int, Task]


@dataclass
class Task:
    title: str
    id: int
    status: TaskStatus
    priority: Priority
    scope: Scope
    notes: str
    time_completed: Optional[datetime] = field(default=None)
    time_created: datetime = field(
        default_factory=lambda: datetime.now().astimezone(ZoneInfo("UTC")))
