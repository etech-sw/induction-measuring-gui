from .Abstract import AbstractCustomerDAO
import mysql.connector as mysql

class CustomerDAO (AbstractCustomerDAO):
    def __connexion(self):
        self.__mDb = mysql.connect(
            host = "localhost",
            user = "root",
            password = "12345678",
            database = "guidatabase"
        )
        self.__mCursor = self.__mDb.cursor()
    

    def register_customer(self, customer):
        self.__connexion()
        request = "INSERT INTO customers (name, surname, email, phone, company, street, location, postal_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (customer.getName(), customer.getSurname(), customer.getEmail(), customer.getPhone(), customer.getCompany(), customer.getStreet(), customer.getLocation(), customer.getPostalCode())
        self.__mCursor.execute(request, value)
        self.__mDb.commit()
        print(f"{self.__mCursor.rowcount}, record inserted")

    
    def delete_customer(self, id_customer):
        self.__connexion()
        request = "DELETE FROM customers WHERE id = %s"
        self.__mCursor.execute(request, (id_customer,))
        self.__mDb.commit()
        print("Deletion is done")

    
    def get_all_customers(self):
        self.__connexion()
        request = "SELECT * FROM customers"
        self.__mCursor.execute(request)
        return self.__mCursor.fetchall()
    

    def get_last_customers(self):
        self.__connexion()
        request = "SELECT * FROM customers ORDER BY id DESC"
        self.__mCursor.execute(request)
        return self.__mCursor.fetchall()


