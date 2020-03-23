# def functionSimple(param1=5):
#     return param1 +1

# print(functionSimple(10))

# def myMethod(param):
#     def innerMethod(p):
#         return p + 1
#     return innerMethod(param)

# print(myMethod(2))

from datetime import datetime
from datetime import timedelta

today = datetime.now()

def myMethod(date):
    def innerMethod(d):
        return d + timedelta(days=2)
    return innerMethod(date)

print("Dans 2 jours nous serons : ", myMethod(today))