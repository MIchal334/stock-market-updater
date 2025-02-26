from concurrent.futures import ThreadPoolExecutor

from application.port.inbound.event_handler import EventHandler
from application.port.outbound.data_updater import DataUpdater
from application.port.outbound.user_informer import UserInformer


class SellerService:
    def __init__(self, event_handler: EventHandler, user_informer: UserInformer, data_updater: DataUpdater):
        self.event_handler = event_handler
        self.user_informer = user_informer
        self.data_updater = data_updater

    def check_events_occurrence(self):
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.businesses_operation)

    def businesses_operation(self):
        event_to_process = self.event_handler.handle_event()
        if event_to_process is None:
            return


