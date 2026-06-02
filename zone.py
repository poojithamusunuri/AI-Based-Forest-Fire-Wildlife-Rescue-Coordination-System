from dataclasses import dataclass

@dataclass
class Zone:
    name: str
    animals_at_risk: int
    risk_level: int
    affected: bool