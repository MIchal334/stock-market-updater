from abc import abstractmethod, ABC


class EventHandler(ABC):

    @abstractmethod
    def handle_event(self) -> EventInfo:
        pass