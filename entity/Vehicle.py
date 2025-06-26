class Vehicle:
    def __init__(self, vehicle_id, model, make, year, color,
                 registration_number, availability, daily_rate):
        self.vehicle_id = vehicle_id
        self.model = model
        self.make = make
        self.year = year
        self.color = color
        self.registration_number = registration_number
        self.availability = availability
        self.daily_rate = daily_rate

    # Getters and Setters
    def get_vehicle_id(self): return self.__vehicle_id
    def set_vehicle_id(self, vehicle_id): self.__vehicle_id = vehicle_id

    def get_model(self): return self.__model
    def set_model(self, model): self.__model = model

    def get_make(self): return self.__make
    def set_make(self, make): self.__make = make

    def get_year(self): return self.__year
    def set_year(self, year): self.__year = year

    def get_color(self): return self.__color
    def set_color(self, color): self.__color = color

    def get_registration_number(self): return self.__registration_number
    def set_registration_number(self, reg_no): self.__registration_number = reg_no

    def is_available(self): return self.__availability
    def set_availability(self, availability): self.__availability = availability

    def get_daily_rate(self): return self.__daily_rate
    def set_daily_rate(self, daily_rate): self.__daily_rate = daily_rate
