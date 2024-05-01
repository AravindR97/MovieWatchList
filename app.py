from database import add_movie, get_movies, watch_movie, get_watched_movies, close_connection, add_user
import datetime

print("Welcome to the watchlist app!\n")

menu = '''Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Exit.


Your selection: '''

def prompt(selection):
    if selection == 4:
        watcher = input("Enter the watcher name: ")
        movie_id = input("Enter the MovieID: ")
        watch_movie(watcher, movie_id)
        return "Watch status updated!\n"
    else:
        title = input("Enter the movie title: ")
        release_date = input("Enter the release date(dd-mm-yyyy): ")
        #convert date string into a datetime object:
        date_object = datetime.datetime.strptime(release_date, "%d-%m-%Y")
        #convert the datetime object into a unix timestamp:
        timestamp = date_object.timestamp()
        add_movie(title, timestamp)
        return "Movie added!\n"

def view(movieList):
    print("\nMOVIE WATCHLIST", "---------------------------------------------------\n", sep= "\n")
    for row in movieList:
        date_obj = datetime.datetime.fromtimestamp(row[2])
        form_date = date_obj.strftime("%d-%m-%Y")
        print(f"{row[0]}. {row[1]} -  {form_date}\n")
    print("\n---------------------------------------------------\n")

def view_watched(movieList):
    print("\nMOVIE WATCHLIST", "---------------------------------------------------\n", sep= "\n")
    for row in movieList:
        print(row[0], "-", row[1])
    print("\n---------------------------------------------------\n")

choice = int(input(menu))

while choice:
    if choice == 1:
        print(prompt(1))
    elif choice == 2:
        view(get_movies(True))
    elif choice == 3:
        view(get_movies())
    elif choice == 4:
        print(prompt(4))
    elif choice == 5:
        view_watched(get_watched_movies(input("Enter the name of the watcher: ")))
    elif choice == 6:
        add_user(input("Enter the name of he User: "))
    elif choice == 7:
        break
    else:
        print("Invalid choice. Try again\n")
    
    choice = int(input(menu))

close_connection()