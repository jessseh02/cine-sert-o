import os
from user.account import login, create_account
from user.movies import display_movies

def main():
    while True:
        print("""
 ██████╗██╗███╗  ██╗███████╗   ███████╗███████╗██████╗ ████████╗ █████╗ ██████╗ 
██╔════╝██║████╗ ██║██╔════╝   ██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗
██║    ██║██╔██╗ ██║█████╗     ███████╗█████╗ ██████╔╝  ██║  ███████║██║  ██║
██║    ██║██║╚██╗██║██╔══╝     ╚════██║██╔══╝ ██╔══██╗  ██║  ██╔══██║██║  ██║
╚██████╗██║██║ ╚████║███████╗   ███████║███████╗██║ ██║  ██║  ██║ ██║╚██████╔╝
 ╚═════╝╚═╝╚═╝ ╚═══╝╚══════╝   ╚══════╝╚══════╝╚═╝ ╚═╝  ╚═╝  ╚═╝ ╚═════╝
BEM VINDO AO CINE SERTÃO! ENTRE NA CONTA PARA COMPRAR INGRESSOS!
""")

        options = int(input("Escolha uma das opções abaixo:\n1 - Entrar na conta\n2 - Criar conta\n3 - Filmes disponíveis\n0 - Sair\n\nDigite a opção: "))

        if options == 1:
            os.system('cls')
            login()
        elif options == 2:
            os.system('cls')
            create_account()
        elif options == 3:
            os.system('cls')
            display_movies()
        elif options == 0:
            print("\nObrigado!\n")
            break

if __name__ == "__main__":
    main()