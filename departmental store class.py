d={ 'milk':20,'jello':10, 'juice':30}
print("MENU :")
print(d)
q=int(input(' enter no. Of items '))
li=list()
for i in range (q):
    item = input(' enter item :')
    li.append(item)
print(li)
total = 0
for i in li:
  if i in d.keys():
         n=int(input(' enter quantity:'))
         bill  = 0
         amt=d.get(i)
         bill = bill+(n*amt)
  total= total+bill
print(total)