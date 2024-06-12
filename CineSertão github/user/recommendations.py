from utils.file_operations import movies, user_preferences

def recommend_movies(user):
    if user in user_preferences:
        preferred_genre = user_preferences[user]
        recommendations = [movie for movie, details in movies.items() if details["Gênero"] == preferred_genre]
        return recommendations
    return []