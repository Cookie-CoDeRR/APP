import argparse
import csv
import json
import re
from pathlib import Path


class Mobile:
    def __init__(self, brand, model, price):
        self.brand = self.validate_text(brand, "Brand")
        self.model = self.validate_text(model, "Model")
        self.price = self.validate_price(price)
        self.category = self.find_category()

    @staticmethod
    def validate_text(value, field_name):
        cleaned_value = str(value).strip()
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 ._-]{0,39}", cleaned_value):
            raise ValueError(f"{field_name} must contain 1 to 40 valid characters")
        return cleaned_value

    @staticmethod
    def validate_price(value):
        try:
            mobile_price = float(value)
        except (TypeError, ValueError) as error:
            raise ValueError("Price must be a number") from error
        if mobile_price < 0:
            raise ValueError("Price cannot be negative")
        return mobile_price

    def find_category(self):
        if self.price >= 60000:
            return "Premium"
        if self.price >= 20000:
            return "Mid-range"
        return "Budget"

    def to_dictionary(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "price": self.price,
            "category": self.category,
        }

    @classmethod
    def from_dictionary(cls, mobile_data):
        return cls(
            mobile_data["brand"],
            mobile_data["model"],
            mobile_data["price"],
        )


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_mobiles(self):
        if not self.mobiles:
            print("No mobiles are available in the store.")
            return

        print(f"{'Brand':<15}{'Model':<20}{'Price':>12}{'Category':>15}")
        print("-" * 62)
        for mobile in self.mobiles:
            print(
                f"{mobile.brand:<15}{mobile.model:<20}"
                f"{mobile.price:>12.2f}{mobile.category:>15}"
            )

    def save_as_json(self, file_path):
        with Path(file_path).open("w", encoding="utf-8") as mobile_file:
            json.dump(
                [mobile.to_dictionary() for mobile in self.mobiles],
                mobile_file,
                indent=4,
            )

    def load_from_json(self, file_path):
        with Path(file_path).open("r", encoding="utf-8") as mobile_file:
            mobile_data = json.load(mobile_file)
        self.mobiles = [Mobile.from_dictionary(item) for item in mobile_data]

    def load_from_csv(self, file_path):
        with Path(file_path).open("r", newline="", encoding="utf-8") as mobile_file:
            mobile_rows = csv.DictReader(mobile_file)
            self.mobiles = [
                Mobile(row["brand"], row["model"], row["price"])
                for row in mobile_rows
            ]


def create_argument_parser():
    argument_parser = argparse.ArgumentParser(
        description="Manage mobile phones in a store."
    )
    argument_parser.add_argument(
        "--data-file",
        default="mobiles.json",
        help="JSON file used to store mobile details.",
    )
    subcommands = argument_parser.add_subparsers(dest="command")

    add_command = subcommands.add_parser("add", help="Add a mobile phone.")
    add_command.add_argument("brand")
    add_command.add_argument("model")
    add_command.add_argument("price", type=float)

    subcommands.add_parser("list", help="Display all mobile phones.")

    import_command = subcommands.add_parser(
        "import-csv",
        help="Import mobile details from a CSV file.",
    )
    import_command.add_argument("csv_file")
    return argument_parser


def run_store_application(arguments):
    mobile_store = Store()
    data_file = Path(arguments.data_file)

    if data_file.exists():
        mobile_store.load_from_json(data_file)

    if arguments.command == "add":
        mobile_store.add_mobile(
            Mobile(arguments.brand, arguments.model, arguments.price)
        )
        mobile_store.save_as_json(data_file)
        print("Mobile added successfully.")
    elif arguments.command == "import-csv":
        mobile_store.load_from_csv(arguments.csv_file)
        mobile_store.save_as_json(data_file)
        print("Mobile data imported successfully.")
    elif arguments.command == "list":
        mobile_store.display_mobiles()
    else:
        print("Choose one of the available commands: add, list, or import-csv.")


def main():
    argument_parser = create_argument_parser()
    arguments = argument_parser.parse_args()
    try:
        run_store_application(arguments)
    except (OSError, KeyError, json.JSONDecodeError, ValueError) as error:
        argument_parser.error(str(error))


if __name__ == "__main__":
    main()