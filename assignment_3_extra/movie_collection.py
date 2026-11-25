import csv
import re


FILENAME = "movies.csv"


def load_movies(filename):
    movies = []
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies.append(row)
    return movies


def display_all(movies):
    if not movies:
        print("No movie records found.")
        return
    print("\n--- Movie Collection ---")
    for m in movies:
        print(f"ID: {m['ID']} | Title: {m['Title']} | Genre: {m['Genre']} | Year: {m['Year']} | Rating: {m['Rating']}")


def search_by_id(movies, movie_id):
    for m in movies:
        if m["ID"] == movie_id:
            print(f"\nID: {m['ID']} | Title: {m['Title']} | Genre: {m['Genre']} | Year: {m['Year']} | Rating: {m['Rating']}")
            return
    print(f"No movie found with ID: {movie_id}")


def search_by_title(movies, keyword):
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    matches = [m for m in movies if pattern.search(m["Title"])]
    if not matches:
        print(f"No movies found matching title: {keyword}")
        return
    print(f"\n--- Movies matching '{keyword}' ---")
    for m in matches:
        print(f"ID: {m['ID']} | Title: {m['Title']} | Genre: {m['Genre']} | Year: {m['Year']} | Rating: {m['Rating']}")


def main():
    movies = load_movies(FILENAME)

    while True:
        print("\n1. Display all movies")
        print("2. Search by Movie ID")
        print("3. Search by title keyword")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            display_all(movies)
        elif choice == "2":
            movie_id = input("Enter Movie ID: ").strip()
            search_by_id(movies, movie_id)
        elif choice == "3":
            keyword = input("Enter title keyword: ").strip()
            search_by_title(movies, keyword)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
