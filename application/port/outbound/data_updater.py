from abc import ABC, abstractmethod


class DataUpdater(ABC):

    @abstractmethod
    def update_user_data(self, user_email: str, current_amount_of_action: int, company_name: str):
        pass
