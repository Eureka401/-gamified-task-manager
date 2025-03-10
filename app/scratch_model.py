from dataclasses import dataclass, field
from enum import Enum, auto
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Optional
from itertools import count
import heapq


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


def make_task(title: str, priority: Priority, notes: str, scope: Scope = Scope.GLOBAL) -> Task:
    task_id = generate_task_id()
    return Task(title, task_id, TaskStatus.TO_DO, priority, scope, notes)


free_task_ids: list[int] = []
START = 1
counter = count(START)


def free_task_id(task_id: int):
    heapq.heappush(free_task_ids, task_id)


def generate_task_id() -> int:
    if free_task_ids:
        return heapq.heappop(free_task_ids)
    return next(counter)
