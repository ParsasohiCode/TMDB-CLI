import requests
import cmd
from colorama import Fore, Style
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Get the API Read Access Token from environment variables
api_read_access_token = os.getenv("API_READ_ACCESS_TOKEN")

headers = {
  "accept": "application/json",
  # use your own API Read Access Token here
  "Authorization": api_read_access_token
}


def response_json(url):
  try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
      return response.json()
  except requests.exceptions.ConnectionError:
    return  "error while connecting to API"

def get_now_playing_movies():
  """Fetch and print popular movies currently playing."""
  response = response_json("https://api.themoviedb.org/3/movie/now_playing")
  if not isinstance(response, dict) or 'results' not in response:
    print(response)
    return
  movies = [movie['title'] for movie in response['results'] if movie.get('popularity', 0) > 200]
  print("Now Playing Popular Movies:")
  for idx, title in enumerate(movies, 1):
    print(Fore.BLUE, idx, Fore.CYAN, title)
  print(Style.RESET_ALL)

def get_popular_movies():
  """Fetch and print popular movies from TMDB."""
  response = response_json("https://api.themoviedb.org/3/movie/popular")
  if not isinstance(response, dict) or 'results' not in response:
    print(response)
    return
  movies = [movie['title'] for movie in response['results']]
  print(Fore.YELLOW, "20 NEW Popular Movies:")
  for idx, title in enumerate(movies, 1):
    print(Fore.BLUE, idx, Fore.CYAN, title)
  print(Style.RESET_ALL)

def get_top_rated_movies():
  """Fetch and print top rated movies from TMDB."""
  response = response_json("https://api.themoviedb.org/3/movie/top_rated")
  if not isinstance(response, dict) or 'results' not in response:
    print(response)
    return
  movies = [movie['title'] for movie in response['results']]
  print(Fore.GREEN, "Top 20 Rated movies based on IMDB ratings:")
  for idx, title in enumerate(movies, 1):
    print(Fore.BLUE, idx, Fore.CYAN, title)
  print(Style.RESET_ALL)

def get_upcoming_movies():
  """Fetch and print upcoming movies from TMDB."""
  response = response_json("https://api.themoviedb.org/3/movie/upcoming")
  if not isinstance(response, dict) or 'results' not in response:
    print(response)
    return
  movies = [movie['title'] for movie in response['results']]
  print(Fore.YELLOW, "20 Upcoming Movies:")
  for idx, title in enumerate(movies, 1):
    print(Fore.BLUE, idx, Fore.CYAN, title)
  print(Style.RESET_ALL)

class MyCLI(cmd.Cmd):
  prompt = '->->->-> '
  intro = 'Welcome to MyCLI. Type "help" for available commands.'

  def do_hello(self, line):
      """Print a greeting."""
      print(Fore.CYAN,"Hello,welcome to MyCLI!. Type 'help' for available commands.", Style.RESET_ALL)
      
  def do_playing(self, line):
      """Print Popular Moives."""
      get_now_playing_movies()
      
  def do_top(self, line):
      """Print all time Top Rated Moives."""
      get_top_rated_movies()
      
  def do_popular(self, line):
      """Print Popular Moives."""
      get_popular_movies()

  def do_upcoming(self, line):
      """Print Upcoming Moives."""
      get_upcoming_movies() 
      
  def do_quit(self, line):
      """Exit the CLI."""
      return True
  def do_exit(self, line):
      """Exit the CLI."""
      return True
  def do_help(self, arg):
    return super().do_help(arg)
  
