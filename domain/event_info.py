from dataclasses import dataclass

from domain.action import Action


@dataclass
class EventInfo:
    client_email: str
    company_name: str
    action: Action
    actionAmount: int

    @staticmethod
    def of(json_dict):
        return EventInfo(client_email=json_dict['client_email'], company_name=json_dict['company_name'],
                         action=Action.of(json_dict['action']), actionAmount=json_dict['actionAmount'])
