import kink

from adapter.inbound.kafka_event_handler import KafkaEventHandler
from adapter.outbound.email_user_informer import EmailUserInformer
from adapter.outbound.sql_data_updtaer import SqlDataUpdater
from application.port.inbound.event_handler import EventHandler
from application.port.outbound.data_updater import DataUpdater
from application.port.outbound.user_informer import UserInformer
from application.seller_service import SellerService


def bootstrap_di():
    event_handler = KafkaEventHandler()
    kink.di[EventHandler] = event_handler
    user_informer = EmailUserInformer()
    kink.di[UserInformer] = user_informer
    data_updater = SqlDataUpdater()
    kink.di[DataUpdater] = data_updater

    seller_service = SellerService(event_handler=event_handler,
                                   user_informer=user_informer,
                                   data_updater=data_updater
                                   )
    kink.di[SellerService] = seller_service
