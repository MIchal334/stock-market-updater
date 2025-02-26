import time

import kink
import schedule

from application.seller_service import SellerService


def init_app_facade_loop():
    schedule.every(5).seconds.do(kink.di[SellerService].check_events_occurrence)


def start_main_loop():
    while True:
        schedule.run_pending()
        time.sleep(0.5)
