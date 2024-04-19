from bson import ObjectId
from Data import server
from Data.models import Guard, Work
from Bussines import operations, guard_service, work_service
from Bussines import smtp

#Get guard data info
guard_data = server.getGuard("Diego", "Rus")
guard = guard_data

#Get works of guard info using his ObjectId for relation and target to a particular month
dataworks = []
try:
    data = server.getWorks(guard.get("_id"))
    listDataWorks = list(data)
    dataworks = operations.filterWorksByMonth(listDataWorks, "03")
except AttributeError as err:
    print(f"ERROR!: ObjectId is null")




guard1 = Guard("","Dario", "Rus", "28-01-1999", "")

#update one work
#server.db.works.update_one({"date": "29-03-2024"}, {"$set": {"total_hours": 11}})



if __name__ == '__main__':
    #Add new Guard
    #print(server.insertGuard(guard1.get_name(), guard1.get_lastName(), guard1.get_dateOfBirth()))

    #Delete one Guard
    #server.deleteGuard(ObjectId('660dd1403add86ed09c59d29'))


    print(f"\nGuard selected: {guard}\n")
    print(operations.viewAllData(dataworks))
    #operations.findDataByDate(data, "29-03-2024")
    print("\n\n")
    (resultPaymetsPerDay, strResultPaymentPerDay) = operations.calculateTotalPaymentPerDay(dataworks)
    print(strResultPaymentPerDay)
    print(f"Total earning = $ {operations.calculateTotalPaymentMonth(resultPaymetsPerDay)}")
    print(f"Total hours = {operations.countTotalHours(dataworks)} hs")

    #Insert new work for a guard
    guard2 = guard_service.getGuard("Diego", "Rus")
    print(guard2.get_guardId(), guard2.get_name(), guard2.get_lastName(), guard2.get_email())
    work2 = Work("", "", '08-04-2024', "Building <Antares I>", "Carlos Pellegrini 1286",
                 "22:00", "06:00",
                 350,"monday")
    work_service.insert_work(guard2, work2)

    #Sending email with worked days and total earnings plus total hours
    message = "Hi Mr. "+guard.get('last_name')+" "+guard.get('name')+"\nYour worked days from March 2024:\n"

    for item in dataworks:
        message += str(item)
        message += "\n"
    result1 = operations.calculateTotalPaymentPerDay(dataworks)
    message += "\nTotal earning = $ "+str(operations.calculateTotalPaymentMonth(resultPaymetsPerDay))
    message += "\nTotal hours = "+str(operations.countTotalHours(dataworks))+" hs"

    print(message)
    #msg = smtp.createMsg(message,"Earnings from March 2024", "diegorus.1992@gmail.com", "diegorus.1992@gmail.com")
    #smtp.sendMsg(msg)


