from dataclasses import dataclass

from domain.action import Action


@dataclass
class EventInfo:
    client_email: str
    company_name: str
    action: Action
    actionAmount: int
