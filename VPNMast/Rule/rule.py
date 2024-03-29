from abc import ABC, abstractmethod
from User.user import user 
from core import Body 

class rule(ABC):
    def __init__(self, name: str, category: int, ip: str, port: str, e_id: int):
        self.name = name
        self.category = category
        self.ip = '127.0.0.1' if ip == 'localhost'else ip
        self.port = port
        self.e_id = e_id
        self.id = 0

    @abstractmethod
    def check(self, user: user, body: Body):
        pass

    def __eq__(self, other):
        if isinstance(other, rule):
            return self.category == other.category and self.ip == other.ip and self.port == other.port and self.e_id == other.e_id
        return False