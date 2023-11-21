
def returnSum(dic):
	
	sum = 0
	for i in dic:
		sum = sum + int(dic[i])
	
	return sum
while True:
    print("\n\n\n\t\t\t ADDING ALL VALUES IN DICTIONARY ")
    print("\t\t\t ------------------------------- ")
    d={}
    n=int(input("\n\n\t\t\t Enter no. of elements  : "))
    for i in range(n):
        key=input("\n\n\t\t\t Enter Key  : ")
        val=input("\n\n\t\t\t Enter Values : ")
        d[key]=val
    print("\n\n\n\t\t\t Given Dictionary : ",d)
    print("\n\n\t\t\t  Sum :", returnSum(d))
    if input("\n\n\t\t Do you wanna continue? : ")!='y':
        print("\n\n\n\t\t -------------------------------------")
        break
