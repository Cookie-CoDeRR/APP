import csv
import argparse


def load_mobiles(filename):
    mobiles = []
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            mobiles.append(row)
    return mobiles


def display_all(mobiles):
    if not mobiles:
        print("No mobile records found.")
        return
    print("\n--- Mobile Store Records ---")
    for m in mobiles:
        print(f"ID: {m['ID']} | Brand: {m['Brand']} | Model: {m['Model']} | Price: {m['Price']}")


def search_by_brand(mobiles, brand):
    matches = [m for m in mobiles if m["Brand"].lower() == brand.lower()]
    if not matches:
        print(f"No mobiles found for brand: {brand}")
        return
    print(f"\n--- Mobiles of Brand: {brand} ---")
    for m in matches:
        print(f"ID: {m['ID']} | Brand: {m['Brand']} | Model: {m['Model']} | Price: {m['Price']}")


def main():
    parser = argparse.ArgumentParser(description="Mobile Store Record System")
    parser.add_argument("--file", required=True, help="Path to the mobiles CSV file")
    args = parser.parse_args()

    mobiles = load_mobiles(args.file)

    while True:
        print("\n1. Display all mobiles")
        print("2. Search by brand name")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            display_all(mobiles)
        elif choice == "2":
            brand = input("Enter brand name: ").strip()
            search_by_brand(mobiles, brand)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
