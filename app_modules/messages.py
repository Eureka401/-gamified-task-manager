from dataclasses import dataclass
from dataclasses import field
from typing import Dict, Any


class Message:
    pass


@dataclass(frozen=True)
class MakeTask(Message):
    title: str
    attributes: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DeleteTask(Message):
    task_id: int
