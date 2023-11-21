while True:
    print("\n\n\n\t\t\t PRINTING HIGHEST LOWEST MARKS")
    print("\t\t\t -----------------------------")

    d={}
    size=int(input("\n\n\t\t\t Enter size : "))
    for i in range(size) :
        key=input("\n\n\t\t\t Enter Name  : ")
        val=input("\n\n\t\t\t Enter Marks : ")
        d[key]=val
    print("\n\n\t\t\t ENTERED DICTIONARIES : ", d)
    highest = max(d.values())
    n = [k for k, v in d.items() if v == highest]

    if len(n)==1:
        print("\n\n\t\t\t",highest,' is the highest mark')

        
    lowest = min(d.values())
    ne = [k for k, v in d.items() if v == lowest]

    if len(ne)==1:
        print("\n\n\t\t\t",lowest,' is the lowest mark')
    
    if input("\n\n\t\t\t Do you wanna continue? : ")!='y':
        print("\n\n\t\t\t --------------------------------------------------------")
        break
