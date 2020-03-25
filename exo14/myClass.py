class MyClass:
    """It's my super class trop bien
    """
    @staticmethod
    def staticmethod(a):
        """ Method to display string in uppercase
        
        Arguments:
            a {str} -- string of your dream
        
        Returns:
            str -- string of your dream, BUT in uppercase ! 
        """
        return a.upper()

print(MyClass.staticmethod("jojo l'astico"))