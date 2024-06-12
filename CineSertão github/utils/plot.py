import matplotlib.pyplot as plt
from utils.file_operations import sold_tickets

def plot_sales_report():
    movie_sales = {}
    for ticket in sold_tickets:
        movie = ticket['movie']
        quantity = ticket['quantity']
        if movie in movie_sales:
            movie_sales[movie] += quantity
        else:
            movie_sales[movie] = quantity

    movies = list(movie_sales.keys())
    quantities = list(movie_sales.values())

    plt.figure(figsize=(10, 5))
    plt.bar(movies, quantities, color='blue')
    plt.xlabel('Filmes')
    plt.ylabel('Ingressos Vendidos')
    plt.title('Relatório de Vendas por Filme')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()