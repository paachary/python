# Class for performing database operations
from data import DatabaseConnection


class DatabaseFunctions:
    id = None
    first_name = ''
    middle_name = ''
    last_name = ''
    age = ''
    emailid = ''
    gender = ''
    phone_id = []
    address_id = []
    bank_id = []
    address_type = []
    door = []
    street = []
    city = []
    state = []
    country = []
    pin = []
    phone_nbr = []
    phone_type = []
    acct_nbr = []
    acct_type = []
    address = []
    bank_name = []
    branch_name = []
    bnk_phone_nbr = []
    connObj = None
    cursor = None

    def __init__(self):
        dbClassName = 'postgresDbConnection'
        dbConn = DatabaseConnection()
        dbConn.setDbType(dbClassName)
        self.connObj = dbConn.getDbConn()
        self.cursor = self.connObj.cursor()

    def __upsertPhoneDtls(self, cursor, id):
        for i in range(len(self.phone_nbr)):
            print(self.phone_id[i], self.phone_nbr[i], self.phone_type[i])
            if (self.phone_id[i] is None):
                print("in insert")
                stmt = """ INSERT INTO personal_phoneinfo AS phoneinfo
                       (person_id, phone_type, phone_nbr) VALUES
                       (%s, %s, %s)
                       ON CONFLICT (person_id, phone_type, phone_nbr)
                       DO NOTHING """
                cursor.execute(stmt,
                               (id,
                                self.phone_type[i],
                                self.phone_nbr[i]))
            else:
                print("in update")
                stmt = """ UPDATE personal_phoneinfo
                           SET phone_nbr = %s,
                               phone_type = %s
                           WHERE id = %s """
                cursor.execute(stmt,
                               (self.phone_nbr[i],
                                self.phone_type[i],
                                self.phone_id[i]))

    def __upsertAddressInfo(self, cursor, id):
        pass

    def __upsertPersonalInfo(self, cursor, id):
        stmt = """ INSERT INTO personal_personalinfo
               (gender, first_name, middle_name, last_name, emailid, age
               ) VALUES
               (%s, %s, %s, %s, %s, %s)
               ON CONFLICT (first_name, middle_name, last_name) DO update
               SET middle_name = %s,
               emailid = %s,
               age = %s"""
        cursor.execute(stmt,
                       (self.gender,
                        self.first_name,
                        self.middle_name,
                        self.last_name,
                        self.emailid,
                        self.age,
                        self.middle_name,
                        self.emailid,
                        self.age))

    def __deleteBankRecords(self, cursor, id):

        stmt = """ SELECT id
                   FROM personal_bankmembership
                   WHERE person_id = %s """
        cursor.execute(stmt, [id])
        row = cursor.fetchone()

        if (row is not None):
            stmt = """ DELETE FROM personal_bankdebitdetails
                       WHERE bankmembership_id = %s """

            cursor.execute(stmt, [row[0]])

            stmt = """ DELETE FROM personal_bankmembership
                   WHERE id = %s """
            cursor.execute(stmt, [row[0]])

    def __deleteAddressRecords(self, cursor, id):
        stmt = """ DELETE FROM personal_addressinfo
                   WHERE person_id = %s """
        cursor.execute(stmt, [id])

    def __deletePhoneRecords(self, cursor, id):
        stmt = """ DELETE FROM personal_phoneinfo
                   WHERE person_id = %s """
        cursor.execute(stmt, [id])

    def __deletePersonalInfo(self, cursor, id):
        stmt = """ DELETE FROM personal_personalinfo
                   WHERE id = %s """
        cursor.execute(stmt, [id])

    def __extractData__(self, jsonData):
        self.id = jsonData.get('person').get('Id')
        self.first_name = jsonData.get('person').get('firstName')
        self.middle_name = jsonData.get('person').get('middleName')
        self.last_name = jsonData.get('person').get('lastName')
        self.gender = jsonData.get('person').get('gender')
        self.age = jsonData.get('person').get('age')
        self.emailid = jsonData.get('person').get('emailid')
        for addresses in jsonData.get('person').get('addresses',
                                                    'no addresses available'):
            if (type(addresses) is str):
                break
            else:
                self.address_id.append(addresses.get('address_id'))
                self.address_type.append(addresses.get('address_type'))
                self.door.append(addresses.get('door'))
                self.street.append(addresses.get('street'))
                self.city.append(addresses.get('city'))
                self.state.append(addresses.get('state'))
                self.country.append(addresses.get('country'))
                self.pin.append(addresses.get('pin'))
        for phones in jsonData.get('person').get('phones',
                                                 'no phones available'):
            if (type(phones) is str):
                break
            else:
                self.phone_id.append(phones.get('phone_id'))
                self.phone_nbr.append(phones.get('phoneNbr'))
                self.phone_type.append(phones.get('phoneType'))
        for bankdtls in jsonData.get('person').get('bankInfo',
                                                   'no bankinfo available'):
            if (type(bankdtls) is str):
                break
            else:
                self.bank_id.append(bankdtls.get('bank_id'))
                self.acct_nbr.append(bankdtls.get('accountNbr'))
                self.acct_type.append(bankdtls.get('accountType'))
                self.address.append(bankdtls.get('address'))
                self.bank_name.append(bankdtls.get('bankName'))
                self.branch_name.append(bankdtls.get('branchName'))
                self.bnk_phone_nbr.append(bankdtls.get('phoneNbr'))

    def __validate__(self, id):
        if (self.id is not None and id != self.id):
            raise ValueError("Passed id value of {0} in the URL is not "
                             "matching the value of id {1} passed "
                             "in the request".format(id, self.id))

    def __updateRecord__(self, id):
        self.__upsertPersonalInfo(self.cursor, id)
        self.__upsertAddressInfo(self.cursor, id)
        self.__upsertPhoneDtls(self.cursor, id)
        self.connObj.commit()
        self.cursor.close()

    def __deleteRecord__(self, id):
        self.__deleteBankRecords(self.cursor, id)
        self.__deletePhoneRecords(self.cursor, id)
        self.__deleteAddressRecords(self.cursor, id)
        self.__deletePersonalInfo(self.cursor, id)
        self.connObj.commit()
        self.cursor.close()

    def upsert(self, id, jsonData):
        self.__extractData__(jsonData)
        self.__validate__(id)
        self.__updateRecord__(id)
        return "Success"

    def delete(self, id):
        self.__validate__(id)
        self.__deleteRecord__(id)
        return "Success"
