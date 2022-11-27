from abc import ABC, abstractmethod


class MyABC(ABC):
    @abstractmethod
    def sayhi(self):
        pass

    @abstractmethod
    def sayBye(self):
        pass

class User(MyABC):
    pass

user = User()
print(user)