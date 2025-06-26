from abc import ABC, abstractmethod

class IAdminService(ABC):

    @abstractmethod
    def get_admin_by_id(self, admin_id):
        pass

    @abstractmethod
    def get_admin_by_username(self, username):
        pass

    @abstractmethod
    def register_admin(self, admin):
        pass

    @abstractmethod
    def update_admin(self, admin):
        pass

    @abstractmethod
    def delete_admin(self, admin_id):
        pass
