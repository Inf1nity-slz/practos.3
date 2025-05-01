import abc

class User(abc.ABC):  
    def __init__(self, username, password, role):
        self._username = username  
        self._password = password  
        self._role = role  
        self._permissions = self.get_permissions()  

    @property
    def username(self):  
        return self._username

    @property
    def role(self): 
        return self._role

    def check_password(self, password):
        return self._password == password 

    @abc.abstractmethod
    def get_permissions(self): 
        pass

    def has_permission(self, permission):
        return permission in self._permissions

    def __str__(self):
        return f"User: {self._username}, Role: {self._role}"


class Admin(User):  
    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    def get_permissions(self): 
        return ["view", "add", "edit", "delete", "sort", "filter"]


class Mechanic(User):  
    def __init__(self, username, password):
        super().__init__(username, password, "mechanic")

    def get_permissions(self): 
        return ["view"]