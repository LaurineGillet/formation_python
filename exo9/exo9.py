# a = [1, 2, 3]
# for ele in a:
#     print(ele)

# b = '123'
# for i in b:
#     print(i)

try:
    a = 124/0

except Exception as e:
    print(e)
finally:
    print('fin')