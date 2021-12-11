#This is just a simple budgeting program made with python.

while True:
    usr = int(input("Enter income: "))
    print("")

    needs = usr * 50/100
    print ("Needs: ", needs)

    wants = usr * 30/100
    print ("Wants: ", wants)

    savings = usr * 20/100
    print ("Savings: ", savings)


    print("")


    print("")
    print("NEEDS")
    print("")

    food = needs * 30/100
    print("Food: ", food)
    
    transport = needs * 25/100
    print("Transport: ", transport)

    watelec = needs * 15/100
    print("Water & Electricity: ", watelec)

    other_needs = needs * 20/100
    print("Other needs: ", other_needs)


    print("")


    print("")
    print("WANTS")
    print("")

    leisure = wants * 30/100
    print("Leisure: ", leisure)

    other_wants = wants * 60/100
    print("Other wants: ", other_wants)


    print("")


    print("")
    print("EXTRA SAVINGS")
    print("")

    extra_sav = (wants * 10/100) + (needs * 10/100)
    print("Extra Savings: ", extra_sav)

    total_sav = savings + extra_sav
    print("Total Savings: ", total_sav)

    print("")
