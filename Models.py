class Customer(object):

    def __init__(self, name, surname, email, phone, company, street, location, postal_code):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__phone = phone
        self.__company = company
        self.__street = street
        self.__location = location
        self.__postal_code = postal_code
    
    def getName(self):
        return self.__name
    
    def getSurname(self):
        return self.__surname

    def getEmail(self):
        return self.__email

    def getPhone(self):
        return self.__phone

    def getCompany(self):
        return self.__company

    def getStreet(self):
        return self.__street

    def getLocation(self):
        return self.__location

    def getPostalCode(self):
        return self.__postal_code


class Device(object):

    def __init__(self, device_manufacturer, type, inductance, dimensions, name, surname):
        self.__device_manufacturer = device_manufacturer
        self.__type = type
        self.__inductance = inductance
        self.__dimensions = dimensions
        self.__nameCustomer = name
        self.__surnameCustomer = surname

    def getDeviceManufacturer(self):
        return self.__device_manufacturer

    def getType(self):
        return self.__type

    def getInductance(self):
        return self.__inductance

    def getDimensions(self):
        return self.__dimensions

    def getNameCustomer(self):
        return self.__nameCustomer

    def getSurnameCustomer(self):
        return self.__surnameCustomer



class Measurement(object):

    def __init__(self, device_id, measure_at, voltage, intensity):
        self.__device_id = device_id
        self.__measure_at = measure_at
        self.__voltage = voltage
        self.__intensity = intensity

    def getDeviceId(self):
        return self.__device_id

    def getMeasureAt(self):
        return self.__measure_at

    def getVoltage(self):
        return self.__voltage

    def getIntensity(self):
        return self.__intensity