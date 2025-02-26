import time

from adapter.outbound import init_adapters
from application import start_main_loop, init_app_facade_loop
from application.bootstraper import bootstrap_di


def start_app():
    bootstrap_di()
    init_adapters()
    init_app_facade_loop()
    time.sleep(1)
    start_main_loop()


if __name__ == '__main__':
    start_app()
