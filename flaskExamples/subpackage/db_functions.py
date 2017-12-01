# Class for performing database operations
from person import Person


class DatabaseFunctions:

    personInfo = None

    def __init__(self):
        pass

    def __extractData__(self, jsonData):
        self.personInfo.setPersonId = jsonData['id']
        self.personInfo.setFirstName = jsonData['firstName']
        self.personInfo.setLastName = jsonData['lastName']
        self.personInfo.setMiddleName = jsonData['middleName']
        self.personInfo.setAge = jsonData['age']
        self.personInfo.setGender = jsonData['gender']

    def __validate__(self, id):
        if id != self.personInfo.getPersonId:
            print("Id not matching")

    def __insertRecord__(self):
        pass

    def __updateRecord__(self, id):
        pass

    def insert(self, jsonData):
        self.personInfo = Person()
        self.__extractData__(jsonData)
        self.__insertRecord__()

    def update(self, id, jsonData):
        self.__extractData__(jsonData)
        self.__validate__(id)
        self.__updateRecord__(id)
        return "Success"
