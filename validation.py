def validate_book(book):

    if not book or len(book.strip()) == 0:
        raise ValueError("Book name cannot be empty")

    if len(book) < 2:
        raise ValueError("Book name is too short")


def validate_user(user):

    if not user or len(user.strip()) == 0:
        raise ValueError("Username cannot be empty")

    if len(user) < 2:
        raise ValueError("Username is too short")
