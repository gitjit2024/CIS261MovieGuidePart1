#Linard Jordan
#CIS261
#Week 6 Lab: Movie Guide Part 2

FILENAME = "movies.txt"

def Write_movies(movies):
    with open(FILENAME, "w") as file:
       for movie in movies:
           file.write(f"{movie}\n")
           
def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file: 
            line = line.replace("\n", "")
            movies.append(line)
        return movies
        

def display_menu():
    print("The Movie List Program")
    
    print()
    
    print("Command Menu")

    print()
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    
def list(movie_list):
    for i , movie in enumerate(movie_list, start = 1):
        print(f"{i}. {movie}")
        print()
        
def add(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added. \n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number. \n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie} was deleted. \n")
        
def main():
    movie_list = ["Cat on a Hot Tin Roof", "On the Waterfront", "Monty Python and the Holy Grail"]
    
    display_menu()
    while True:
        command = input("Command: ")
        if command.lower() =="list":
            list(movie_list)
        elif command.lower() =="add":
            add(movie_list)
        elif command.lower() =="del":
            delete(movie_list)
        elif command.lower() =="exit":
            break
        else:
            print("not a valid command, please try again. \n")
           
    print("Bye!")
            
if __name__ == "__main__":
    main()
        

