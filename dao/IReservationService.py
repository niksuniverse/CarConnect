from abc import ABC, abstractmethod

class IReservationService(ABC):

    @abstractmethod
    def get_reservation_by_id(self, reservation_id):
        pass

    @abstractmethod
    def get_reservations_by_customer_id(self, customer_id):
        pass

    @abstractmethod
    def create_reservation(self, reservation):
        pass

    @abstractmethod
    def update_reservation(self, reservation):
        pass

    @abstractmethod
    def cancel_reservation(self, reservation_id):
        pass
