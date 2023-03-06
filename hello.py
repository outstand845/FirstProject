def Paging(m, n):
    if(m%n == 0):
        return m//n
    else:
        return m//n+1
print(Paging(5,10))
print(Paging(15,10))
print(Paging(25,10))
print(Paging(30,10))