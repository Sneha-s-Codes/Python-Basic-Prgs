while True:
    print("\n\n\n\t\t\t PRINTING ALL UNIQUE VALUES IN DICTIONARY ")
    print("\t\t\t ---------------------------------------- ")
    l=[{"Desktop":"s001"},{"Laptop":"s002"},{"Desktop":"s001"},{"LED TV":"s005"},{"LED TV":"s005"},{"Washing Machine":"s009"},{"Clock":"s007"}]
    print("\n\t\t\t ORIGINAL LIST : ", l)
    uni=set(val for dic in l for val in dic.values())
    print("\n\n\t\t\t UNIQUE VALUES : ", uni)
    if input("\n\n\t\t\t Do you wanna continue? : ")!='y':
        print("\n\t\t\t -------------------------------------------------------------------")
        break