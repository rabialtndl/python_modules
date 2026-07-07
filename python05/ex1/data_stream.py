from typing import Any
import abc


class DataStream(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0
    
    def register_processor(self, proc: DataProcessor) -> None: