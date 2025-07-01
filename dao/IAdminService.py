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

    @abstractmethod
    def authenticate(self, username, password):
        pass

    @abstractmethod
    def get_reservation_history(self):
        pass

    @abstractmethod
    def get_vehicle_utilization(self):
        pass

    @abstractmethod
    def get_revenue_summary(self):
        pass

    @abstractmethod
    def get_top_vehicles_by_revenue(self):
        pass

    @abstractmethod
    def get_most_active_customers(self):
        pass

    @abstractmethod
    def get_least_utilized_vehicles(self):
        pass

    @abstractmethod
    def get_monthly_revenue_trend(self):
        pass

    @abstractmethod
    def get_reservation_status_summary(self):
        pass

    @abstractmethod
    def get_booking_by_weekday(self):
        pass

    @abstractmethod
    def get_inactive_customers(self):
        pass
