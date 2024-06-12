import os
from admin.manage_movies import manage_movies
from admin.manage_users import manage_users
from admin.reports import manage_reports
from admin.promotions import manage_promotions
from utils.file_operations import admins  # Adicione esta linha para importar 'admins'

def create_admin_account():
    user = str(input('Digite seu usuário: '))
    password = str(input('Digite sua senha: '))
    if user in admins:
        input('\nUsuário já existe! Pressione Enter para voltar...')
    else:
        admins[user] = [user, password]
        input('\nCadastro realizado! Pressione Enter para voltar...\n')
    os.system('cls')

def admin_menu(user_login):
    while True:
        optionsAdmin = int(input("Escolha uma das opções abaixo:\n1 - Gerenciar Filmes\n2 - Gerenciar usuários\n3 - Criar conta admin\n4 - Relatórios\n5 - Promoções\n0 - Sair\n\nDigite a opção: "))
        os.system('cls')
        if optionsAdmin == 0:
            break
        elif optionsAdmin == 1:
            manage_movies()
        elif optionsAdmin == 2:
            manage_users()
        elif optionsAdmin == 3:
            create_admin_account()
        elif optionsAdmin == 4:
            manage_reports()
        elif optionsAdmin == 5:
            manage_promotions()
        else:
            print("Opção inválida.")