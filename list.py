m=input().split()
n=int(input())
s=[]
for i in range(1,n+1):
    for j in m:
        s.append(f"{j}{i}")
print(s)