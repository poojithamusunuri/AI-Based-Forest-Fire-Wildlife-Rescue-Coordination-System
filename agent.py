from dataclasses import dataclass

@dataclass
class Agent:
    agent_id: int
    agent_type: str
    location: str
    available: bool