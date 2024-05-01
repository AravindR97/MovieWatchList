from database import add_movie, get_movies, watch_movie, get_watched_movies
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
    title = input("Enter the movie title: ")
    if selection == 4:
        watch_movie(title)
        return "Watch status updated!\n"
    else:
        release_date = input("Enter the release date(dd-mm-yyyy): ")
        #convert date string into a datetime object:
        date_object = datetime.datetime.strptime(release_date, "%d-%m-%Y")
        #convert the datetime object into a unix timestamp:
        timestamp = date_object.timestamp()
        add_movie(title, timestamp)
        return "Movie added!\n"

def view(movieList):
    print("\nMOVIE WATCHLIST", "---------------------------------------------------\n", sep= "\n")
    for num, row in enumerate(movieList):
        date_obj = datetime.datetime.fromtimestamp(row[1])
        form_date = date_obj.strftime("%d-%m-%Y")
        print(f"{num+1}. {row[0]} on  {form_date}\n")
    print("\n---------------------------------------------------\n")

choice = int(input(menu))

while choice:
    if choice == 1:
        print(prompt())
    elif choice == 2:
        view(get_movies(True))
    elif choice == 3:
        view(get_movies())
    elif choice == 4:
        print(prompt(4))
    elif choice == 5:
        view(get_watched_movies())
    elif choice == 6:
        print("Work in progress. Come back soon!\n")
    elif choice == 7:
        pass
    else:
        print("Invalid choice. Try again\n")
    
    choice = int(input(menu))