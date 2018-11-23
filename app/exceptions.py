class ApplicationError(Exception):
    msg = "Application error."


class WrongClustersNumberError(ApplicationError):
    def __init__(self, msg):
        self.msg = msg


class MatrixParsingError(ApplicationError):
    msg = "Error when parsing str matrix."
