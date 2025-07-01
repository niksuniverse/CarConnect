
class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address, username, password,
                     registration_date):
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
        return self._password == password

    # customer_id property
    @property
    def customer_id(self):
        return self._customer_id
    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    # first_name property
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    # last_name property
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    # email property
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = value

    # phone_number property
    @property
    def phone_number(self):
        return self._phone_number
    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    # address property
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, value):
        self._address = value

    # username property
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, value):
        self._username = value

    # password property
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value

    # registration_date property
    @property
    def registration_date(self):
        return self._registration_date
    @registration_date.setter
    def registration_date(self, value):
        self._registration_date = value
