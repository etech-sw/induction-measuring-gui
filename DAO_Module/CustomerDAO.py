from .Abstract import AbstractCustomerDAO
import mysql.connector as mysql

class CustomerDAO (AbstractCustomerDAO):
    def __connexion(self):
        self.__mDb = mysql.connect(
            host = "127.0.0.1",
            user = "appuser",
            password = "hund1234",
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


    def update_customer(self, customer, id_customer):
        self.__connexion()
        request = "UPDATE customers SET name = %s, surname = %s, email = %s, phone = %s, company = %s, street = %s, location = %s, postal_code = %s WHERE id = %s"
        value = (customer.getName(), customer.getSurname(), customer.getEmail(), customer.getPhone(), customer.getCompany(), customer.getStreet(), customer.getLocation(), customer.getPostalCode(), id_customer)
        self.__mCursor.execute(request, value)
        self.__mDb.commit()
        print(f"Informations about {customer.getSurname()} are updated !")

        