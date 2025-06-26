class Customer:
    def __init__(self, customer_id,first_name, last_name, email, phone_number,
                 address, username, password, registration_date):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.username = username
        self.password = password
        self.registration_date = registration_date

    def authenticate(self, password):
        return self.__password == password

    #Getters and Setters
    def get_customer_id(self): return self.__customer_id
    def set_customer_id(self, customer_id): self.__customer_id = customer_id

    def get_first_name(self): return self.__first_name
    def set_first_name(self, first_name): self.__first_name = first_name

    def get_last_name(self): return self.__last_name
    def set_last_name(self, last_name): self.__last_name = last_name

    def get_email(self): return self.__email
    def set_email(self, email): self.__email = email

    def get_phone_number(self): return self.__phone_number
    def set_phone_number(self, phone): self.__phone_number = phone

    def get_address(self): return self.__address
    def set_address(self, address): self.__address = address

    def get_username(self): return self.__username
    def set_username(self, username): self.__username = username

    def get_password(self): return self.__password
    def set_password(self, password): self.__password = password

    def get_registration_date(self): return self.__registration_date
    def set_registration_date(self, date): self.__registration_date = date
