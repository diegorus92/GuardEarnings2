
def viewAllData(data):
    worked_days = 0

    for item in data:
        print(item)
        worked_days += 1
    print(f"Worked days: {worked_days}")

def findDataByDate(data, date = "01-03-2024"):
    for item in data:
        if item.get('date') == date:
            print(item)

def filterWorksByMonth(data, monthNumber):
    data_filtered = list(filter(lambda s: str("-"+monthNumber+"-") in s.get("date"), data))
    return data_filtered
def calculateTotalPaymentPerDay(data):
    payments = []

    for item in data:
        #total = item.get('total_hours') * item.get('payment_per_hours')
        total = calculateTotalHoursWorked(item.get('checkIn'), item.get('checkOut')) * item.get('payment_per_hours')
        payments.append(total)
        print(f"Total payment {item.get('day')} {item.get('date')} = $ {total}")

    return payments

def calculateTotalPaymentMonth(list_payments_per_days):
    acumulator = 0
    for payment in list_payments_per_days:
        acumulator += payment
    return acumulator


######Calculate Hours between checkIn and checkOut
def calculateTotalHoursWorked(checkIn, checkOut):
    entrance = list(map(lambda x: int(x), checkIn.split(':')))
    exit = list(map(lambda x: int(x), checkOut.split(':')))
    hours = _calculateHours(entrance[0], exit[0])
    minutes = _calculateMinutes(entrance[1], exit[1])

    if entrance[1] > exit[1]:
        return (hours - minutes)
    else:
        return (hours + minutes)

def _calculateHours(entranceH, exitH):
    limit = 24
    acumulator = 0
    counter = entranceH

    while counter != exitH:
        if counter == limit:
            counter = 0
        acumulator += 1
        counter += 1

    return acumulator

def _calculateMinutes(entranceM, exitM):
    return (entranceM + exitM) / 60

def countTotalHours(data):
    counter = 0
    for item in data:
        counter += calculateTotalHoursWorked(item.get('checkIn'), item.get('checkOut'))
    return counter