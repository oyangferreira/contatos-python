class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contato adicionado com sucesso.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contato removido com sucesso.")
                return
        print("Contato não encontrado.")

    def list_contacts(self):
        if not self.contacts:
            print("Nenhum contato disponível.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print("Contato não encontrado.")
