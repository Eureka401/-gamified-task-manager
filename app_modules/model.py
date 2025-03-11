from project_types import TaskDatabase, AppError
from dataclasses import dataclass, field
from itertools import count
import heapq
from typing import Optional

from abc import ABC, abstractmethod


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


@dataclass(frozen=True)
class Model:
    task_database: TaskDatabase = field(default_factory=dict)
    task_id_generator: TaskIDGenerator = field(
        default_factory=lambda: Default(1))
    error: Optional[AppError] = None
