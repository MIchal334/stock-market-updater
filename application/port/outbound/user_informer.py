from abc import ABC, abstractmethod


class UserInformer(ABC):

    @abstractmethod
    def send_info_to_user(self, user_email: str, info: str) -> None:
        pass
