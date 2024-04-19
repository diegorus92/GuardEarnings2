class Guard:
    def __init__(self, guardId, name, last_name, date_of_birth, email):
        self._guardId = guardId
        self._name = name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._email = email

    def get_guardId(self):
        return self._guardId

    def get_name(self):
        return self._name

    def get_lastName(self):
        return self._last_name

    def get_dateOfBirth(self):
        return self._date_of_birth

    def get_email(self):
        return self._email

class Work:
    def __init__(self, workId, guardId, date, place, address, checkIn, checkOut, paymentPerHours, day):
        self._workid = workId
        self._guarId = guardId
        self._date = date
        self._place = place
        self._address = address
        self._checkIn = checkIn
        self._checkOut = checkOut
        self._paymentPerHours = paymentPerHours
        self._day = day


    def get_WorkId(self):
        return self._workid

    def get_GuardId(self):
        return self._guarId

    def get_date(self):
        return self._date

    def get_place(self):
        return self._place

    def get_address(self):
        return self._address

    def get_checkIn(self):
        return self._checkIn

    def get_checkOut(self):
        return self._checkOut

    def get_paymentPerHours(self):
        return self._paymentPerHours

    def get_day(self):
        return self._day