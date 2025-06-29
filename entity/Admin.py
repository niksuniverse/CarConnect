class Admin:
    def __init__(self, admin_id, first_name, last_name, email, phone_number,
                 username, password, role, join_date):
        self.admin_id = admin_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.role = role
        self.join_date = join_date

    def authenticate(self, password):
        return self.__password == password

    # Getters and Setters
    def get_admin_id(self):
        return self.__admin_id
    def set_admin_id(self, admin_id):
        self.__admin_id = admin_id

    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_phone_number(self): return (
        self.__phone_number)
    def set_phone_number(self, phone):
        self.__phone_number = phone

    def get_username(self):
        return self.__username
    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return (self.__password)
    def set_password(self, password):
        self.__password = password

    def get_role(self):
        return self.__role
    def set_role(self, role):
        self.__role = role

    def get_join_date(self): return (
        self.__join_date)
    def set_join_date(self, join_date):
        self.__join_date = join_date
