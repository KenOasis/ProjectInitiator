class Error(Exception):
    """Base class for other exceptions"""
    pass

class WrongFileStructInfoError(Error):
    """
        Raised when the format of the struct_info is incorrected 
    """
    pass

class WrongFilePathError(Error):
    """
        when struct_info is List[str], some of path of str not format
        correctly. Pls check Format.md to check the corrent format
    """
    pass

class InitialProjectError(Error):
    """
        Raised when initial project failed
    """
    pass