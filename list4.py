my_list=input().split()
a=0
for i in range(1,len(my_list),2):
    a=my_list[i]
    my_list[i]=my_list[i-1]
    my_list[i-1]=a
print(my_list)