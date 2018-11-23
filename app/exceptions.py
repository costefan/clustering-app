class ApplicationError(Exception):
    msg = "Application error."


class WrongClustersNumberError(ApplicationError):
    msg = ""


class MatrixParsingError(ApplicationError):
    msg = "Error when parsing str matrix."
