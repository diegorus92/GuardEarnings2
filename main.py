import calendar
import datetime

from bson import ObjectId
from Data import server
from Data.models import Guard, Work
from Bussines import operations, guard_service, work_service
from Bussines import smtp


if __name__ == '__main__':
    workMonthTarget = "04"

    #Insert new work for a guard
    guard2 = guard_service.getGuard("Diego", "Rus")
    work2 = Work("", "", '19-04-2024', "Building <Antares I>", "Carlos Pellegrini 1286",
                 "22:00", "06:00",
                 400,"friday")
    #work_service.insert_work(guard2, work2)



    #Sending email with worked days and total earnings plus total hours
    message = ("Hi Mr. "+guard2.get_lastName()+" "+guard2.get_name()+
               "\nYour worked days for "+str(calendar.month_name[int(workMonthTarget)])+":\n")

    dataworks = list(operations.filterWorksByMonth(server.getWorks(guard2.get_guardId()), workMonthTarget))
    dataworks.sort(key=lambda x: x["date"], reverse=False) #Works list sorted by date
    for item in dataworks:
        message += str(item)
        message += "\n"
    (resultPaymetsPerDay, strPaymentPerDay) = operations.calculateTotalPaymentPerDay(dataworks)
    message += "\n\n"+strPaymentPerDay
    message += "\nTotal earning = $ "+str(operations.calculateTotalPaymentMonth(resultPaymetsPerDay))
    message += "\nTotal hours = "+str(operations.countTotalHours(dataworks))+" hs"

    print(message)
    #msg = smtp.createMsg(message,"Earnings from April 2024", "diegorus.1992@gmail.com", str(guard2.get_email()))
    #smtp.sendMsg(msg)

