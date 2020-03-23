class Error(Exception):
   """Base class for other exceptions"""
   pass

class AmphoraFileNotFoundError(Error):
   """Raised when the input value is too small"""
   pass
