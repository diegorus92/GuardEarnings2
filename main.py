from bson import ObjectId
from Data import server
from Data.models import Guard
from Bussines import operations

#Get guard data info
guard_data = server.getWorksByGuard("Diego", "Rus")
guard = guard_data

#Get works of guard info using his ObjectId for relation and target to a particular month
dataworks = []
try:
    data = server.getWorks(guard.get("_id"))
    listDataWorks = list(data)
    dataworks = operations.filterWorksByMonth(listDataWorks, "03")
except AttributeError as err:
    print(f"ERROR!: ObjectId is null")



work = {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '05-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286', 'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350, 'day': 'tuesday'}
works = [
    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '09-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '20:00', 'checkOut': '08:00',
        'total_hours': 12, 'payment_per_hours': 350,
        'day': 'saturday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '10-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '20:00', 'checkOut': '06:00',
        'total_hours': 10, 'payment_per_hours': 350,
        'day': 'sunday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '11-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'monday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '12-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'tuesday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '13-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'wednesday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '14-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'thursday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '15-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'friday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '16-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '20:00', 'checkOut': '08:00',
        'total_hours': 12, 'payment_per_hours': 350,
        'day': 'saturday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '17-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '20:00', 'checkOut': '06:00',
        'total_hours': 10, 'payment_per_hours': 350,
        'day': 'sunday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '18-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'monday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '19-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'tuesday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '20-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'wednesday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '21-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'thursday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '22-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'friday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '23-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '20:00', 'checkOut': '08:00',
        'total_hours': 12, 'payment_per_hours': 350,
        'day': 'saturday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '24-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '20:00', 'checkOut': '06:00',
        'total_hours': 10, 'payment_per_hours': 350,
        'day': 'sunday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '25-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'monday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '26-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'tuesday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '27-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'wednesday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '28-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'thursday'},

    {'guard_id': ObjectId('660b21c8bae8e3b85f5a99d1'),
        'date': '29-03-2024', 'place': 'Building <Antares I>',
        'address': 'Carlos Pellegrini 1286',
        'checkIn': '22:00', 'checkOut': '06:00',
        'total_hours': 8, 'payment_per_hours': 350,
        'day': 'friday'}
]

guard1 = Guard("Dario", "Rus", "28-01-1999")

#update one work
#server.db.works.update_one({"date": "29-03-2024"}, {"$set": {"total_hours": 11}})



if __name__ == '__main__':
    #Add new Guard
    #print(server.insertGuard(guard1.get_name(), guard1.get_lastName(), guard1.get_dateOfBirth()))

    #Delete one Guard
    #server.deleteGuard(ObjectId('660dd1403add86ed09c59d29'))

    for guardItem in list(server.getGuards()):
        print(guardItem)

    print(f"\nGuard selected: {guard}\n")
    operations.viewAllData(dataworks)
    #operations.findDataByDate(data, "29-03-2024")
    print("\n\n")
    result = operations.calculateTotalPaymentPerDay(dataworks)
    print(f"Total earning = $ {operations.calculateTotalPaymentMonth(result)}")
    print(f"Total hours = {operations.countTotalHours(dataworks)} hs")

    #print(operations.calculateTotalHoursWorked("20:30", "07:00"))


