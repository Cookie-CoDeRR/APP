# library_system.py
# made using local model openai.gpt-oss-20b MLX 4bit quantized

from __future__ import annotations
import uuid
from dataclasses import dataclass, field
from typing import Dict, List

# --------------------------------------------------------------------------- #
#   Data models
# --------------------------------------------------------------------------- #

@dataclass(eq=True, frozen=True)
class Book:
    """Represents a book in the library."""
    title: str
    author: str
    isbn: str  # unique identifier


@dataclass(eq=True, frozen=True)
class User:
    """Represents a library user."""
    name: str
    email: str
    uid: str = field(default_factory=lambda: str(uuid.uuid4()))

# --------------------------------------------------------------------------- #
#   Library core
# --------------------------------------------------------------------------- #

class Library:
    """Simple in‑memory library system."""

    MAX_BORROWED = 5

    def __init__(self) -> None:
        # maps isbn → Book
        self._books: Dict[str, Book] = {}
        # maps uid   → User
        self._users: Dict[str, User] = {}
        # maps isbn → uid (who has borrowed it)
        self._loans: Dict[str, str] = {}

    # --------------------- book handling ----------------------------------- #
    def add_book(self, title: str, author: str, isbn: str) -> None:
        if isbn in self._books:
            raise ValueError(f"ISBN {isbn} already exists.")
        self._books[isbn] = Book(title, author, isbn)

    def remove_book(self, isbn: str) -> None:
        if isbn not in self._books:
            raise KeyError(f"No book with ISBN {isbn}.")
        if isbn in self._loans:
            raise RuntimeError(f"Book {isbn} is currently borrowed.")
        del self._books[isbn]

    # --------------------- user handling ----------------------------------- #
    def add_user(self, name: str, email: str) -> User:
        # Ensure no duplicate emails
        if any(u.email == email for u in self._users.values()):
            raise ValueError(f"Email {email} already registered.")
        user = User(name, email)
        self._users[user.uid] = user
        return user

    def remove_user(self, uid: str) -> None:
        if uid not in self._users:
            raise KeyError(f"No user with id {uid}.")
        # cannot remove if the user still has books
        borrowed = [isbn for isbn, borrower in self._loans.items() if borrower == uid]
        if borrowed:
            raise RuntimeError(f"User {uid} still has books: {borrowed}.")
        del self._users[uid]

    # --------------------- borrowing --------------------------------------- #
    def borrow_book(self, uid: str, isbn: str) -> None:
        if uid not in self._users:
            raise KeyError(f"Unknown user id {uid}.")
        if isbn not in self._books:
            raise KeyError(f"Unknown ISBN {isbn}.")
        if isbn in self._loans:
            raise RuntimeError(f"Book {isbn} already borrowed by user {self._loans[isbn]}.")
        # check user's current loans
        if sum(1 for b in self._loans.values() if b == uid) >= self.MAX_BORROWED:
            raise RuntimeError(f"User {uid} has reached the borrowing limit ({self.MAX_BORROWED}).")
        self._loans[isbn] = uid

    def return_book(self, uid: str, isbn: str) -> None:
        if isbn not in self._loans or self._loans[isbn] != uid:
            raise RuntimeError(f"User {uid} does not hold book {isbn}.")
        del self._loans[isbn]

    # --------------------- helpers ---------------------------------------- #
    def list_books(self) -> List[Book]:
        return list(self._books.values())

    def list_users(self) -> List[User]:
        return list(self._users.values())

    def current_loans(self) -> Dict[str, str]:
        """Return a copy of the loan mapping (isbn → uid)."""
        return dict(self._loans)

# --------------------------------------------------------------------------- #
#   Demo (run when this file is executed directly)
# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    lib = Library()

    # Add users
    alice = lib.add_user("Alice Smith", "alice@example.com")
    bob   = lib.add_user("Bob Jones",  "bob@example.com")

    # Add books
    lib.add_book("1984", "George Orwell", "978-0451524935")
    lib.add_book("Brave New World", "Aldous Huxley", "978-0060850524")

    # Alice borrows 1984
    lib.borrow_book(alice.uid, "978-0451524935")

    # Show current state
    print("Books:", lib.list_books())
    print("Users:", lib.list_users())
    print("Loans:", lib.current_loans())

    # Alice returns 1984
    lib.return_book(alice.uid, "978-0451524935")

    # Final state
    print("\nAfter return:")
    print("Loans:", lib.current_loans())
