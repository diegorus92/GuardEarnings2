class Guard:
    def __init__(self, name, last_name, date_of_birth):
        self._name = name
        self._last_name = last_name
        self._date_of_birth = date_of_birth

    def get_name(self):
        return self._name

    def get_lastName(self):
        return self._last_name

    def get_dateOfBirth(self):
        return self._date_of_birth

