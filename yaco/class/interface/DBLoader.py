import abc
class DBLoader(metaclass=abc.ABCMeta):
    @abstractmethod
    def load_data(self,info):
        raise NotImplementedError