l1=[]
n= int(input("range :"))
for i in range(n):
    e=int(input(""))
    l1.append(e)

l2=[]
n= int(input("range :"))
for i in range(n):
    e=int(input(""))
    l2.append(e)

l3=[]
n= int(input("range :"))
for i in range(n):
    e=int(input(""))
    l3.append(e)
    
print("list 1 : " ,l1)
print("list 2 : ", l2)
print("list 3 : ", l3)

print("\n\t COMMON VALUES ARE : ", set(l1) & set(l2) & set(l3))
