class LenGetError(Exception):
    """
    Класс для пользовательской ошибки.
    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"LenGetError: {self.message}"


class LenNotProvidedError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"LenNotProvided: {self.message}"


class TypeGetError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"TypeGetError: {self.message}"


class DateGetError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"DateGetError: {self.message}"
