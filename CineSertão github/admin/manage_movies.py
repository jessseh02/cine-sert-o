import os
from utils.file_operations import movies

def manage_movies():
    while True:
        manage_movies = int(input("Escolha uma das opções abaixo:\n1 - Adicionar filme\n2 - Remover filme\n3 - Atualizar dados do filme\n0 - Voltar\n\nDigite a opção: "))
        os.system("cls")

        if manage_movies == 0:
            break

        if manage_movies == 1:
            add_movie = str(input('Digite o nome do filme: '))
            if add_movie in movies:
                input('\nFilme já existe! Pressione Enter para continuar...')
                continue
            add_director = str(input('Digite o nome do diretor: '))
            add_genre = str(input('Digite o nome do gênero: '))
            add_room = str(input('Digite o número da sala: '))
            add_price = str(input('Digite o preço do filme: '))
            add_ticket = str(input('Digite quantos ingressos tem: '))
            add_time = str(input('Digite o horário do filme: '))
            if add_movie in movies:
                input('\nFilme já existe! Pressione Enter para voltar...')
                continue
            else:
                movies[add_movie] = {
                    "Diretor": add_director,
                    "Gênero": add_genre,
                    "Sala": add_room,
                    "Horário": add_time,
                    "Ingressos": add_ticket,
                    "Preço": add_price
                }
                input('\nFilme adicionado! Pressione Enter para voltar...\n')

        elif manage_movies == 2:
            search_movie = str(input('Digite o nome do filme: '))
            if search_movie in movies.keys():
                movies.pop(search_movie)
                os.system('cls')
                print("Filme removido!\n")
            elif search_movie not in movies.keys():
                input('Filme não está no catálogo ou não está escrito corretamente!\nPressione Enter para voltar...\n')

        elif manage_movies == 3:
            movie_to_update = str(input('Digite o nome do filme que deseja atualizar: '))
            if movie_to_update in movies:
                print("\nQual informação você gostaria de atualizar?")
                print("1 - Diretor")
                print("2 - Gênero")
                print("3 - Sala")
                print("4 - Horário")
                print("5 - Ingressos")
                print("6 - Preço")
                update_option = int(input("\nDigite a opção: "))

                if update_option == 1:
                    new_director = str(input("Digite o novo diretor: "))
                    movies[movie_to_update]["Diretor"] = new_director
                elif update_option == 2:
                    new_genre = str(input("Digite o novo gênero: "))
                    movies[movie_to_update]["Gênero"] = new_genre
                elif update_option == 3:
                    new_room = str(input("Digite a nova sala: "))
                    movies[movie_to_update]["Sala"] = new_room
                elif update_option == 4:
                    new_time = str(input("Digite o novo horário: "))
                    movies[movie_to_update]["Horário"] = new_time
                elif update_option == 5:
                    new_tickets = int(input("Digite a nova quantidade de ingressos: "))
                    movies[movie_to_update]["Ingressos"] = new_tickets
                elif update_option == 6:
                    new_price = str(input("Digite o novo preço: "))
                    movies[movie_to_update]["Preço"] = new_price
                else:
                    print("Opção inválida.")

                print("\nInformações atualizadas com sucesso!")
            else:
                print("\nFilme não encontrado.")
            input("\nPressione Enter para voltar...")
            os.system('cls')