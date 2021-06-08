def func_del(a, b):
    while b==0:
         print('Error,division by zero')
         b= int(input('Enter another number:'))
    res=a/b
    return res
print(func_del(a= int(input('Enter a:')), b = int((input('Enter b:')))))