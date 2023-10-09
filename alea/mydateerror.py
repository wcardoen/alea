from . import mydate

class MyDateError(Exception):
    """
    Date Error Class
    """
    def __init__(self, code):
        """
        Constructor of the Date Error class
        """
        self.code = code

    def __str__(self):
        """
        Overloading of the str function
        :return:
        """
        return repr(self.code)
