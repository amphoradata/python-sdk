from logging import getLogger
logger = getLogger('errors.py')


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ApiError(Error):
    """ The API returned an error code. """
    pass


class AmphoraFileNotFoundError(Error):
    """The Amphora does not contain a file by that name"""
    pass


class FileExistsError(Error):
    """The local file already exists"""
    def __init__(self, path: str):
        logger.error(f'The local file {path} aready exists.')


class SignalNotExistError(Error):
    """The signal doesn't exist on the Amphora"""
    def __init__(self, _property: str):
        logger.error(
            f'A signal with property {_property} does not exist on this Amphora.'
        )


class InvalidDataError(Error):
    """The data is invalid"""
    def __init__(self, message: str):
        logger.error(f'The data is invalid, {message}')


class InvalidDataStructure(Error):
    """The data structure is invalid"""
    def __init__(self, message: str):
        logger.error(f'The data is invalid. {message}')
