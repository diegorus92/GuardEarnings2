from Data import server
from Data.models import Guard

def getGuard(guardName, guardLastName):
    guardtemp = server.getGuard(guardName, guardLastName)
    guard = Guard(
        guardtemp.get('_id'),
        str(guardtemp.get('name')), str(guardtemp.get('last_name')),
        str(guardtemp.get('date_of_birth')), str(guardtemp.get('email'))
    )
    return guard