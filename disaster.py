from dataclasses import dataclass

@dataclass
class Disaster:
    disaster_type: str
    severity: int
    location: str
    affected_population: int
    status: str