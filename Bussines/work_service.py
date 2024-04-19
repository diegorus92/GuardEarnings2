from Data import server, models

def insert_work(guard, workToAdd):
    work = {
        "guard_id": guard.get_guardId(),
        'date': workToAdd.get_date(),
        "place": str(workToAdd.get_place()),
        "address": str(workToAdd.get_address()),
        "checkIn": str(workToAdd.get_checkIn()), "checkOut": str(workToAdd.get_checkOut()),
        "payment_per_hours": workToAdd.get_paymentPerHours(), "day": str(workToAdd.get_day())
    }

    print(server.insertWork(work))
