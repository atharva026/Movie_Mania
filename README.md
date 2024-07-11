# [Movie Mania](https://atharvamane03.pythonanywhere.com)

Welcome to Movie Mania! This web application allows users to search for movies and get detailed information about their favorite films using the OMDB API.

## Introduction

Movie Mania is a simple and user-friendly web application that leverages the OMDB API to provide detailed information about movies. Users can search for movies by title and get information such as the plot, cast, director, release date, and more.

## Features

- Search for movies by title
- Display detailed information about the movies
- User-friendly interface

## Technologies Used

- HTML
- Tailwind CSS
- Django
- Python
- OMDB API

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/atharva026/Movie_Mania.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Movie_Mania
    ```

3. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

4. Install the dependencies:

    ```bash
    pip install django
    ```

5. Get your API key from [OMDB API](http://www.omdbapi.com) and add it to the project in settings.py .
   ```bash
    OMDB_API_KEY='your_api_key'
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://localhost:8000`.
2. Use the search bar to enter the title of a movie you want to find.
3. Click on the search button to fetch and display the movie details.

## Contact

For any inquiries or feedback, please reach out to:

- Email: atharvam99@gmail.com

Happy Coding!
