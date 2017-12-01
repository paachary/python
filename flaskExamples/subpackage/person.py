class Person:

    person_id = None
    firstName = ''
    lastName = ''
    middleName = ''
    age = None
    gender = ''
    # phones = Phones
    # addresses = Addresses
    # bankDetails = BankDetails

    def __init__(self):
        pass

    def getPersonId(self):
        return self.person_id

    def setPersonId(self, person_id):
        self.person_id = person_id

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getMiddleName(self):
        return self.middleName

    def setMiddleName(self, middleName):
        self.middleName = middleName

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender
