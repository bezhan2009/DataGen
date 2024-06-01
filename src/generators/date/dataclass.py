from datetime import datetime


class Date:
    """
    Represents a generated date and optional time.

    :param date: The generated date.
    """

    def __init__(self, date: datetime) -> None:
        self.date: datetime = date

    def __str__(self) -> str:
        """Returns the string representation of the generated date."""
        return self.date.isoformat()

    def __repr__(self) -> str:
        """Returns the official string representation of the generated date."""
        return f"GeneratedDate(date={self.date})"
