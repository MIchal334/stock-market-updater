from abc import abstractmethod, ABC

from domain.event_info import EventInfo


class EventHandler(ABC):

    @abstractmethod
    def handle_event(self) -> EventInfo:
        pass