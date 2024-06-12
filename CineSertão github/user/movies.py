import os
from utils.file_operations import movies, sold_tickets, save_ticket_to_file, user_preferences
from user.recommendations import recommend_movies

def display_movies():
    print("Filmes disponíveis:")
    for movie, infos in movies.items():
        print(f"\nFilme: {movie}")
        print(f"Diretor: {infos['Diretor']}")
        print(f"Gênero: {infos['Gênero']}")
        print(f"Sala: {infos['Sala']}")
        print(f"Horário: {infos['Horário']}")
        print(f"Ingressos: {infos['Ingressos']}")
        print(f"Preço: R${infos['Preço']}")
    input("\nPressione Enter para voltar...")
    os.system('cls')

def user_menu(user_login):
    while True:
        optionsUser = int(input("Escolha uma das opções abaixo:\n1 - Comprar Ingressos\n2 - Filmes disponíveis\n3 - Ver recomendações\n0 - Voltar\n\nDigite a opção: "))
        if optionsUser == 0:
            break
        elif optionsUser == 1:
            os.system('cls')
            print("Escolha um filme para comprar ingressos:")
            counter = 0
            for movie in movies.keys():
                counter += 1
                print(f"{counter} - {movie}")
            movie_choice = int(input("\nDigite o número do filme: "))
            movie_list = list(movies.keys())

            if 1 <= movie_choice <= len(movies):
                selected_movie = movie_list[movie_choice - 1]
                print(f"\nVocê selecionou {selected_movie}.")
                tickets = int(input("Quantos ingressos você gostaria de comprar?: "))

                if tickets <= movies[selected_movie]["Ingressos"]:
                    movies[selected_movie]["Ingressos"] -= tickets
                    total_price = tickets * float(movies[selected_movie]["Preço"].replace(",", "."))
                    print(f"\nCompra realizada com sucesso! {tickets} ingressos para {selected_movie}.")
                    sold_tickets.append({
                        "user": user_login,
                        "movie": selected_movie,
                        "quantity": tickets,
                        "total_price": total_price
                    })
                    save_ticket_to_file({
                        "user": user_login,
                        "movie": selected_movie,
                        "quantity": tickets,
                        "total_price": total_price
                    })
                    user_preferences[user_login] = movies[selected_movie]["Gênero"]
                else:
                    print(f"\nDesculpe, não há ingressos suficientes disponíveis para {selected_movie}.")

                input("\nPressione Enter para voltar...")
            os.system('cls')
        elif optionsUser == 2:
            os.system('cls')
            display_movies()
        elif optionsUser == 3:
            os.system('cls')
            recommendations = recommend_movies(user_login)
            if recommendations:
                print("Recomendações baseadas nas suas preferências:")
                for movie in recommendations:
                    print(f"- {movie}")
            else:
                print("Nenhuma recomendação disponível.")
            input("\nPressione Enter para voltar...")
            os.system('cls')
        else:
            print("Opção inválida.")