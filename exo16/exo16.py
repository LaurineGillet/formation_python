import logging


class MyClass:
    @staticmethod
    def staticmethod(up):
        logging.warning('Attention')
        logging.error('erreur')
        logging.critical('critique')
        logging.log(50, "aformac")
        return up.upper()


print(MyClass.staticmethod('stringtoupper'))