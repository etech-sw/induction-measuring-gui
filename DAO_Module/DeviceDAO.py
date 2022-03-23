from urllib import request
from .Abstract import AbstractDeviceDAO
import mysql.connector as mysql

class DeviceDAO(AbstractDeviceDAO):
    def __connexion(self):
        self.__mDb = mysql.connect(
            host = "localhost",
            user = "appuser",
            password = "hund1234",
            database = "guidatabase"
        )
        self.__mCursor = self.__mDb.cursor()

    
    def register_device(self, device):
        self.__connexion()
        request = "INSERT INTO devices (device_manufacturer, type, inductance, dimensions, name_customer, surname_customer) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (device.getDeviceManufacturer(), device.getType(), device.getInductance(), device.getDimensions(), device.getNameCustomer(), device.getSurnameCustomer())
        verification = "SELECT * FROM customers WHERE name = %s AND surname = %s"
        self.__mCursor.execute(verification, (device.getNameCustomer(), device.getSurnameCustomer()))
        # On verifie si le customer en question existe deja dans la base de donnees, et si oui, alors on effectu l'enregistrement
        # du device.
        if (len(self.__mCursor.fetchall()) != 0):
            self.__mCursor.execute(request, value)
            self.__mDb.commit()
            print(f"{self.__mCursor.rowcount}, record inserted")
            return True
        else:
            return False
    

    def delete_device(self, id_device):
        self.__connexion()
        request = "DELETE FROM devices WHERE id = %s"
        self.__mCursor.execute(request, (id_device,))
        self.__mDb.commit()
        print("Deletion is done")

    
    def get_all_devices(self):
        self.__connexion()
        request = "SELECT * FROM devices"
        self.__mCursor.execute(request)
        return self.__mCursor.fetchall()

    
    def get_last_devices(self):
        self.__connexion()
        request = "SELECT * FROM devices ORDER BY id DESC"
        self.__mCursor.execute(request)
        return self.__mCursor.fetchall()

    
    def update_device(self, device, id_device):
        self.__connexion()
        request = "UPDATE devices SET device_manufacturer = %s, type = %s, inductance = %s, dimensions = %s, name_customer = %s, surname_customer = %s WHERE id = %s"
        value = (device.getDeviceManufacturer(), device.getType(), device.getInductance(), device.getDimensions(), device.getNameCustomer(), device.getSurnameCustomer(), id_device)
        verification = "SELECT * FROM customers WHERE name = %s AND surname = %s"
        self.__mCursor.execute(verification, (device.getNameCustomer(), device.getSurnameCustomer()))
        if (len(self.__mCursor.fetchall()) != 0):
            self.__mCursor.execute(request, value)
            self.__mDb.commit()
            print(f"Informations about device are updated !")
            return True
        else:
            return False

        