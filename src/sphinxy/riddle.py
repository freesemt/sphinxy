from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    """A class representing a riddle."""
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """Check if the given answer is correct."""
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """Get a hint for the riddle"""
        yield from iter(self.answer)
