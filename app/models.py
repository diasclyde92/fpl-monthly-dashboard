from dataclasses import dataclass, field


@dataclass
class Manager:
    entry: int
    player_name: str
    entry_name: str
    total: int
    rank: int
    history: list = field(default_factory=list)


@dataclass
class MonthlyScore:
    manager: str
    team: str
    month: str
    points: int