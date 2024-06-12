import os

def manage_promotions():
    while True:
        promo_options = int(input("Escolha uma das opções abaixo:\n1 - Criar Promoção\n2 - Gerenciar Promoções\n0 - Voltar\n\nDigite a opção: "))
        if promo_options == 0:
            break
        elif promo_options == 1:
            promo_name = str(input("Digite o nome da promoção: "))
            promo_discount = float(input("Digite o desconto (em %): "))
            print(f"Promoção {promo_name} com {promo_discount}% de desconto criada com sucesso!")
        elif promo_options == 2:
            print("Gerenciar promoções ainda não implementado.")
        input("\nPressione Enter para voltar...")
        os.system('cls')