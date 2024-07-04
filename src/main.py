from contact import Contact
from contact_manager import ContactManager

def main():
    manager = ContactManager()

    while True:
        print("\nGerenciador de Contatos")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Listar Contatos")
        print("4. Procurar Contato")
        print("0. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Digite o nome: ")
            phone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            contact = Contact(name, phone, email)
            manager.add_contact(contact)
        elif choice == '2':
            name = input("Digite o nome do contato a ser removido: ")
            manager.remove_contact(name)
        elif choice == '3':
            manager.list_contacts()
        elif choice == '4':
            name = input("Digite o nome do contato a ser procurado: ")
            manager.search_contact(name)
        elif choice == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
