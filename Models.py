class Client(object):

    def __init__(self, name, surname, email, phone, company, street, location, postal_code):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.company = company
        self.street = street
        self.location = location
        self.postal_code = postal_code
    
    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone

    def getCompany(self):
        return self.company

    def getStreet(self):
        return self.street

    def getLocation(self):
        return self.location

    def getPostalCode(self):
        return self.postal_code


class Dispositif(object):

    def __init__(self, device_manufacturer, type, inductance, dimensions, name, surname):
        self.device_manufacturer = device_manufacturer
        self.type = type
        self.inductance = inductance
        self.dimensions = dimensions
        self.nameClient = name
        self.surnameClient = surname

    def getDeviceManufacturer(self):
        return self.device_manufacturer

    def getType(self):
        return self.type

    def getInductance(self):
        return self.inductance

    def getDimensions(self):
        return self.dimensions

    def getNameClient(self):
        return self.nameClient

    def getSurnameClient(self):
        return self.surnameClient