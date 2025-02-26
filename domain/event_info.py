from dataclasses import dataclass

from domain.action import Action


@dataclass
class EventInfo:
    client_email: str
    company_name: str
    action: Action
    action_amount: int

    @staticmethod
    def of(json_dict):
        return EventInfo(client_email=json_dict['clientEmail'], company_name=json_dict['companyName'],
                         action=Action.of(json_dict['action']), action_amount=json_dict['actionAmount'])
