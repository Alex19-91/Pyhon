def factori_al(num):
    fir_st=1
    if num ==0:
        yield f'{num}!=1'
    for i in range(1,num+1):
        fir_st*=i
        yield  f'{i}!={fir_st}'

for el in factori_al(int(input('Enter a number:'))):
    print(el)
