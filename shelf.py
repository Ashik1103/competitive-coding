n=int(input("enter"))

for i in range(0,n):
    a,b,c =list(map(int,input().split()))
    
    if b>c:
        o=2
        while True:
            new_box=c+o
            if new_box>b:
                print(a*o)
                break
            else:
                o=o+1
    elif b<=c:
        print(a)
    
                

