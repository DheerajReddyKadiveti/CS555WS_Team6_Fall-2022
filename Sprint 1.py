
import datetime
from prettytable import PrettyTable

dateList=[]
#getting name using IDs
def getNameUsingID(individualList, ID):
    for i in individualList:
        if(i[0] == ID):
            return i[1]
#For the individual list

def individualList():
    ilist = [0 for i in range(7)]
    ilist[5] = []
    return ilist

	
#For the family list
def familyList():
    flist = [0 for i in range(6)]
    flist[5] = []
    return flist

#get last name
def lastName(s):
    temp=''
    for i in s:
        if(i != '/'):
            temp += i
    return temp

#get today's date
def currentDate():
    currDate = str(datetime.date.today())
    
    return currDate

#Converting date into a standard format
def convertDateFormat(date):
    temp = date.split()
    if(temp[1] == 'JAN'): temp[1] = '01'
    if(temp[1] == 'FEB'): temp[1] = '02'
    if(temp[1] == 'MAR'): temp[1] = '03'
    if(temp[1] == 'APR'): temp[1] = '04'
    if(temp[1] == 'MAY'): temp[1] = '05'
    if(temp[1] == 'JUN'): temp[1] = '06'
    if(temp[1] == 'JUL'): temp[1] = '07'
    if(temp[1] == 'AUG'): temp[1] = '08'
    if(temp[1] == 'SEP'): temp[1] = '09'
    if(temp[1] == 'OCT'): temp[1] = '10'
    if(temp[1] == 'NOV'): temp[1] = '11'
    if(temp[1] == 'DEC'): temp[1] = '12'
    if(temp[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        temp[2] = '0' + temp[2]
    return (temp[0] + '-' + temp[1] + '-' + temp[2])

dateList = []
todayDate = currentDate()

#User Story 1
## This function gets dates before today's date
def DatesBeforeCurrentDate(indiListData, famListData):
  
  #for individual
    for i in indiListData:
        if(str(i[3]) > todayDate):
            dateList.append(i[3])
            print(i[3] + " : " + i[0] + " is before today's date")
        if(i[4] != 0):
            if(str(i[4]) > todayDate):
                dateList.append(i[4])
                print(i[4] + " : " + i[0] + " is before today's date")
	#for family
    for i in famListData:
        if(str(i[3]) > todayDate):
            dateList.append(i[3])
            print(i[3] + " : " + i[0] + " is before today's date")
        if(str(i[4]) != 0):
            if(str(i[4]) > todayDate):
                dateList.append(i[4])
                print(i[4] + " : " + i[0] + " is before today's date")
    if(len(dateList) == 0):
        print("There are no dates before today's date")
    else:
        print("There dates after today's date ")
        print(dateList)

#User Story 2 
#This function is to get all the marriage dates
def getMarriageDatesUsingID(famListData, id):
    for i in famListData:
        if(i[0] == id):
            return i[3]
			
def BirthBeforeMarriage(indiListData, famListData):
    for i in indiListData:
        birthDate = i[3]
        if(i[5] != []):
            for j in i[5]:
                if(birthDate > getMarriageDatesUsingID(famListData, j)): #We call the function here to get the dates
                    dateList.append(i[1])
                    print(i[1] + " have their marriage dates before birth date")
                    break
    if(len(dateList) == 0):
        print("After the date of marriage,nobody is born ")
    else:
        print("These individuals' birth dates after their marriage dates")
        print(dateList)
	
#User Story 3
		
def BirthBeforeDeath(indiListData):
    for i in indiListData:
        if(i[4] != 0):
            if(i[3] > i[4]):
                dateList.append(i[1])
                print(i[1] + " had their birth date after death date")
    if(len(dateList) == 0):
        print("After the date of death,nobody is born")
    else:
        print("These individuals' birth dates come after their marriage dates ")
        print(dateList)
#User Story 4

def MarriageBeforeDivorce(famListData):
    for i in famListData:
        if(i[4] != 0):
            if(i[3] > i[4]):
                dateList.append(i[0])
                print(i[0] + " had their wedding date after their divorce date")
    if(len(dateList) == 0):
        print("After the date of the divorce, nobody gets married ")
    else:
        print("These individuals' wedding dates come after their divorce dates ")
        print(dateList)
		
#This function returns all the death dates
def getDeathDateByID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            if(i[4] != 0):
                return i[4]

