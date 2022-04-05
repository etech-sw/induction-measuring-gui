from urllib import request
from .Abstract import AbstractDeviceDAO
import mysql.connector as mysql

class MeasurementDAO(AbstractDeviceDAO):
    def __connexion(self):
        self.__mDb = mysql.connect(
            host = "localhost",
            user = "appuser",
            password = "hund1234",
            database = "guidatabase"
        )
        self.__mCursor = self.__mDb.cursor()

    def get_all_measurements(self, device_id, start_measurement):
        self.__connexion()
        request = "SELECT measure_at, voltage, intensity FROM measurement WHERE device_id = %s AND measure_at >= %s ORDER By id DESC"
        self.__mCursor.execute(request, (device_id, start_measurement))
        return self.__mCursor.fetchall()

        