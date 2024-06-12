import os
from utils.file_operations import users

def manage_users():
    while True:
        manage_users = int(input("Escolha uma das opções abaixo:\n1 - Remover Usuário\n2 - Atualizar Dados de Usuário\n3 - Buscar Usuário\n0 - Sair\n\nDigite a opção: "))

        if manage_users == 0:
            break

        elif manage_users == 1:
            os.system('cls')
            search_user = str(input('Digite o nome do usuário que deseja remover: '))
            found_users = [user for user in users.keys() if search_user.lower() in user.lower()]
            if found_users:
                print("\nUsuários encontrados:")
                for idx, user in enumerate(found_users):
                    print(f"{idx + 1} - {user}")
                user_choice = int(input("\nDigite o número do usuário que deseja remover: "))
                if 1 <= user_choice <= len(found_users):
                    selected_user = found_users[user_choice - 1]
                    users.pop(selected_user)
                    print(f"\nUsuário {selected_user} removido com sucesso!")
                else:
                    print("\nOpção inválida.")
            else:
                print("\nNenhum usuário encontrado com esse nome.")
            input("\nPressione Enter para voltar...")
            os.system('cls')

        elif manage_users == 2:
            user_to_update = str(input('Digite o nome do usuário que deseja atualizar: '))
            if user_to_update in users:
                print("\nQual informação você gostaria de atualizar?")
                print("1 - Nome de Usuário")
                print("2 - Senha")
                update_option = int(input("\nDigite a opção: "))

                if update_option == 1:
                    new_username = str(input("Digite o novo nome de usuário: "))
                    if new_username in users:
                        print("\nEste nome de usuário já existe. Tente outro.")
                    else:
                        users[new_username] = users.pop(user_to_update)
                        print("\nNome de usuário atualizado com sucesso!")
                elif update_option == 2:
                    new_password = str(input("Digite a nova senha: "))
                    users[user_to_update][1] = new_password
                    print("\nSenha atualizada com sucesso!")
                else:
                    print("Opção inválida.")
            else:
                print("\nUsuário não encontrado.")
            input("\nPressione Enter para voltar...")
            os.system('cls')

        elif manage_users == 3:
            os.system('cls')
            search_user = str(input('Digite o nome do usuário: '))
            found_users = [user for user in users.keys() if search_user.lower() in user.lower()]
            if found_users:
                print("\nUsuários encontrados:")
                for user in found_users:
                    print(f"- {user}")
            else:
                print("\nNenhum usuário encontrado com esse nome.")
            input("\nPressione Enter para voltar...")
            os.system('cls')