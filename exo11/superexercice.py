from titrepro import TitrePro 
from aformac import Aformac

class SuperExercice(TitrePro, Aformac):
    EXERCICE = 'dev'
    __techno = 'Python'

    def exercer(self):
        print("Coucou l'aformac je fais mes modules")

SuperExercice().distance()