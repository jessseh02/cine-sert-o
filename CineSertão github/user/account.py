import os
from user.movies import user_menu
from admin.admin_menu import admin_menu  # Update the import statement
from utils.file_operations import users, admins

def login():
    print("""
┏┓                        
┣ ┏┓╋┏┓┏┓┏┓ ┏┓┏┓ ┏┏┓┏┓╋┏┓
┗┛┛┗┗┛ ┗┻┛  ┛┗┗┻ ┗┗┛┛┗┗┗┻
""")
    user_login = str(input('Digite seu usuário: '))
    password_login = str(input('Digite sua senha: '))

    if user_login in users and users[user_login][1] == password_login:
        os.system('cls')
        print('Login realizado com sucesso!\n')
        user_menu(user_login)
    elif user_login in admins and admins[user_login][1] == password_login:
        os.system('cls')
        print('Login realizado com sucesso!\n')
        admin_menu(user_login)
    else:
        print("Usuário ou senha incorretos.")

def create_account():
    print("""
┏┓ •             
┃ ┏┓┓┏┓┏┓ ┏┏┓┏┓╋┏┓
┗┛┛ ┗┗┻┛  ┗┗┛┛┗┗┗┻
""")
    user = str(input('Digite seu usuário: '))
    password = str(input('Digite sua senha: '))
    if user in users:
        input('\nUsuário já existe! Pressione Enter para voltar...')
    else:
        users[user] = [user, password]
        input('\nCadastro realizado! Pressione Enter para voltar...\n')
    os.system('cls')