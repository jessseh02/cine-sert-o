import os
from utils.file_operations import sold_tickets
from utils.plot import plot_sales_report

def generate_report():
    with open("relatorio_vendas.txt", "w") as file:
        for ticket in sold_tickets:
            file.write(f"Usuário: {ticket['user']}, Filme: {ticket['movie']}, Quantidade: {ticket['quantity']}, Preço Total: {ticket['total_price']}\n")

def generate_movie_report(movie_name):
    with open(f"relatorio_{movie_name}.txt", "w") as file:
        found = False
        for ticket in sold_tickets:
            if ticket['movie'] == movie_name:
                found = True
                file.write(f"Usuário: {ticket['user']}, Quantidade: {ticket['quantity']}, Preço Total: {ticket['total_price']}\n")
        if not found:
            file.write("Nenhum ingresso vendido para este filme.\n")

def manage_reports():
    while True:
        report_options = int(input("Escolha uma das opções abaixo:\n1 - Relatório de Vendas\n2 - Relatório de Vendas por Filme\n3 - Visualizar Gráfico de Vendas\n0 - Voltar\n\nDigite a opção: "))
        if report_options == 0:
            break
        elif report_options == 1:
            generate_report()
            print("Relatório de vendas gerado com sucesso!")
        elif report_options == 2:
            movie_name = str(input("Digite o nome do filme: "))
            generate_movie_report(movie_name)
            print(f"Relatório de vendas para {movie_name} gerado com sucesso!")
        elif report_options == 3:
            plot_sales_report()
        input("\nPressione Enter para voltar...")
        os.system('cls')