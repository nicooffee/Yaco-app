import abc
class DBWriter(metaclass=abc.ABCMeta):
    @abstractmethod
    def add_data(self):
        raise NotImplementedError
    def del_data(self):
        raise NotImplementedError