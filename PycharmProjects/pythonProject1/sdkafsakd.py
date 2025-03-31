def a(x,y):
    total1=0
    total2=0
    for i in range(1,x):
        if x % i ==0:
            total1 +=1
    for j in range(1,y):
        if y % j ==0:
            total2 +=1
    if total1 == total2:
        return True
    else:
        return False
print(a(3,3))