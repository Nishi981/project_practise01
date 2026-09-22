#input list and remove dublications
l=[]
k=[]
n=int(input("enter number of elements"))
for i in range(n):
    item=int(input("enter elements:"))
    l.append(item)
unique_list=set(l)
for item in unique_list:
    print(item)    