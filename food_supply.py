n=int(input())

for i in range(n):
    a,b,c,d,e=list(map(int,input().split()))
    tem=a/c
    temp=b/d
    
    if tem>=e:
        
        if temp>=e:
            print("yes")
        else:
            print("no")
    else:
        print("no")
