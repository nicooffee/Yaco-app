from abc import ABCMeta,abstractmethod
class DBWriter(metaclass=ABCMeta):
    @abstractmethod
    def add_data(self,connection,*arg):
        raise NotImplementedError
    @abstractmethod
    def del_data(self,connection,*arg):
        raise NotImplementedError