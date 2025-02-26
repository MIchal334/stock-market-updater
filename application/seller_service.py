from concurrent.futures import ThreadPoolExecutor

from application.port.inbound.event_handler import EventHandler
from application.port.outbound.data_updater import DataUpdater
from application.port.outbound.user_informer import UserInformer
from domain.event_info import EventInfo

EMAIL_TEMPLATE = "Market info. Operation {}. Company name {}. Current amount of action: {}"


class SellerService:
    def __init__(self, event_handler: EventHandler, user_informer: UserInformer, data_updater: DataUpdater):
        self.event_handler = event_handler
        self.user_informer = user_informer
        self.data_updater = data_updater

    def check_events_occurrence(self):
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.__businesses_operation)

    def __businesses_operation(self):
        print("START BUISSNES PROCESS")
        event_to_process = self.event_handler.handle_event()
        if event_to_process is None:
            return

        print(f"EVENT {event_to_process}")
        current_action_amount = self.data_updater.get_current_amount_of_action(user_email=event_to_process.client_email,
                                                                               company_name=event_to_process.company_name)

        action_amount_after_action = event_to_process.action.apply(current_action_amount, event_to_process.action_amount)

        self.data_updater.update_user_data(user_email=event_to_process.client_email,
                                           company_name=event_to_process.company_name,
                                           current_amount_of_action=action_amount_after_action)

        self.user_informer.send_info_to_user(user_email=event_to_process.client_email,
                                             info=self.__create_information_for_user(event=event_to_process,
                                                                                     action_amount_after_action=action_amount_after_action))

    @staticmethod
    def __create_information_for_user(event: EventInfo, action_amount_after_action: int) -> str:
        return EMAIL_TEMPLATE.format(event.action.value, event.company_name, action_amount_after_action)
