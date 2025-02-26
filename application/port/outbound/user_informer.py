from abc import ABC, abstractmethod

from domain.action import Action


class UserInformer(ABC):

    @abstractmethod
    def send_info_to_user(self, user_email: str, action: Action, company_name: str) -> None:
        pass
