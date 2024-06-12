users = {"abc": ["abc", "123"]}
admins = {"Filipe": ["Filipe", "Maciel"], "Jesseh": ["Jesseh", "Albuquerque"]}
movies = {
    "Interestelar": {
        "Diretor": "Christopher Nolan",
        "Gênero": "Ficção Científica",
        "Sala": "1",
        "Horário": "20:00",
        "Ingressos": 5,
        "Preço": "20,00"
    },
    "Django Livre": {
        "Diretor": "Quentin Tarantino",
        "Gênero": "Faroeste",
        "Sala": "2",
        "Horário": "20:00",
        "Ingressos": 25,
        "Preço": "25,00"
    },
    "Forrest Gump O Contador de Histórias": {
        "Diretor": "Robert Zemeckis",
        "Gênero": "Comédia",
        "Sala": "3",
        "Horário": "20:00",
        "Ingressos": 30,
        "Preço": "15,00"
    },
}

sold_tickets = []  # Lista para armazenar os ingressos vendidos
user_preferences = {}  # Dicionário para armazenar as preferências dos usuários

def save_ticket_to_file(ticket_info):
    with open(f"compra_{ticket_info['user']}_{ticket_info['movie']}.txt", "w") as file:
        file.write(f"Usuário: {ticket_info['user']}\n")
        file.write(f"Filme: {ticket_info['movie']}\n")
        file.write(f"Quantidade: {ticket_info['quantity']}\n")
        file.write(f"Preço Total: {ticket_info['total_price']}\n")