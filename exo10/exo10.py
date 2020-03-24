def decorate_upper(func):
    def custom_upper():
        return func().upper()
    return custom_upper

@decorate_upper
def test():
    return "Hello les girlz"

print(test()) 


# def decorate(func):
#     def func_custom(*args, **kwargs):
#         print("Function paramater {0}".format(func))
#         return func


def decorate_cut(func):
    def custom_cut():
        return func()[0:5]
    return custom_cut

@decorate_cut
def hoho():
    return "Coucou, comment que ça va bien ?"

print(hoho())