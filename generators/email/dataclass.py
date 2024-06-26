class Email:
    """
    Represents a generated email address.

    :param email: The generated email address.
    """

    def __init__(self, email: str) -> None:
        self.email: str = email

    def __str__(self) -> str:
        """Returns the string representation of the generated email."""
        return self.email

    def __len__(self):
        """Returns the length of the generated email."""
        return len(self.email)

    def __repr__(self) -> str:
        """Returns the official string representation of the generated email."""
        return f"GeneratedEmail(email={self.email})"
