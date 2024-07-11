from django.shortcuts import redirect, render
import requests
from django.conf import settings

def fetchDetails(title):
    return f"http://www.omdbapi.com/?t={title}&apikey={settings.OMDB_API_KEY}"


def index(request):
    movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Fight Club"]
    movie_data = []

    for title in movies:
        response = requests.get(fetchDetails(title))
        data = response.json()
        if data['Response'] == 'True':  # Check if the movie data was fetched successfully
            movie_data.append(data)

    return render(request, 'movie_search_form.html', {'movies': movie_data})


def movie_search(request):
    title = request.GET.get('title')
    if title:
        response = requests.get(fetchDetails(title))
        data = response.json()
        # print(data)

        # Checking if movie data was found
        if data and 'Title' in data:
            return render(request, 'movie_details.html', {'movie': data})
        else:
            return render(request, 'movie_details.html', {'movie': False})
    else:
        return redirect('movie_search_form')