n=int(input ())

for i in range(0,n):
#    locals()["x" + str(i),"y"+str(i)]=list(map(int,input("enter x and y").split()))

#    locals()["a" + str(i)] = "abc"  
    a,b=list(map(int,input().split()))
    totF=a*10
    totS=b*90
    total=totF+totS
    print(total)



