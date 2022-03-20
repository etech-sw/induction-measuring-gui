from abc import ABC

class AbstractCustomerDAO(ABC):
    
    # Enregistrer un customer
    def register_customer (customer):
        pass

    # Supprimer un customer
    def delete_customer (id_customer):
        pass

    # Recuperer la liste des customers
    def get_all_customers():
        pass

    # Recuperer la liste des derniers customers
    def get_last_customers():
        pass

    # Modification des donnees d'un customer
    def update_customer (customer, id_customer):
        pass


class AbstractDeviceDAO(ABC):

    # Enregistrer un device
    def register_device (device):
        pass

    # Supprimer un device
    def delete_device (id_device):
        pass

    # Recuperer la liste des devices
    def get_all_devices():
        pass

    # Recuperer la liste des derniers devices
    def get_last_devices():
        pass

    # Modification des donnees d'un device
    def update_device (device, id_device):
        pass