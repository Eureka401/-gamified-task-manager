from dataclasses import dataclass, field
from enum import Enum, auto
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Optional
from itertools import count
import heapq

from abc import ABC, abstractmethod


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


class TaskIDGenerator(ABC):
    @abstractmethod
    def free_task_id(self, task_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def generate(self) -> int:
        raise NotImplementedError


class Default(TaskIDGenerator):
    def __init__(self, seed: int):
        self._start = seed
        self._free_task_ids: list[int] = []
        self._counter = count(self._start)

    def free_task_id(self, task_id: int):
        heapq.heappush(self._free_task_ids, task_id)

    def generate(self) -> int:
        if self._free_task_ids:
            return heapq.heappop(self._free_task_ids)
        return next(self._counter)


class TaskManagementModel:
    def __init__(self, task_id_generator: TaskIDGenerator, task_database: Task_DB) -> None:
        self.task_database = task_database
        self.task_id_generator = task_id_generator

    def make_task(self, title: str, notes: str, priority: Priority = Priority.NONE, scope: Scope = Scope.GLOBAL):
        task_id = self.task_id_generator.generate()
        self.save_task_to_db(
            Task(title, task_id, TaskStatus.TO_DO, priority, scope, notes))

    def save_task_to_db(self, task: Task):
        key = task.id
        task_database[key] = task


task_database: Task_DB = {}
default_task_id_generator = Default(1)
model = TaskManagementModel(default_task_id_generator, task_database)
