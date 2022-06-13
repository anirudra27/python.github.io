#Importing date time to get date and time automatically
import datetime

#This is function that displays welcome message
def welcome():
    print("===========================================================================")
    print("||\t\t\t\t\t\t\t\t\t ||")
    print("|| \t\t\tWelcome to Bike Management\t\t\t ||")
    print("===========================================================================\n\n")

#This function calls date time module and returns current date and time
def getTime():
    current_time = str(datetime.datetime.now())
    return current_time

#This function reads bikes.txt file and converts it to 2dlist
def _list():
    #This is same as f3=open('Bikes.txt','r')
    with open('Bikes.txt', 'r') as f3:
        result = []
        for line in f3:
            words = line.split(',')
            result.append((words[0:]))
    return result

#This function displays options and take an option from user and validates it and calls the chosen function
def options():
    print("Press any of following number to select an option")
    print("1. Display bikes")
    print("2. Add Stock")
    print("3. Purchase bikes")
    print("4. Add new bike")
    print("5. Exit the program\n")

    option = 0
    while not option in range(1,7):
        try:
            option = int(input("Enter your choice: "))
        except:
            print("\n\nPlease enter a valid number between 1-10:\n")

    if option > 5 or option < 1:
        print("\nInvalid Option! Select only number listed below")
        options()
    elif(option == 1):
        displayBike()
    elif(option == 2):
        addStock()
    elif(option == 3):
        purchaseBike()
    elif(option == 4):
        addBike()
    elif(option == 5):
        print("Goodbye!")
        quit()

#this function displays 2dlist for bikes in tabular form
def showBike():
    result = _list()
    bikeID = 1
    print("ID\tBike Name\t\tCompany Name\t\t\t\t\t Color\t\t     Quantity\tprice")
    for v in result:
        name, brand, color, quantity, price = v
        print ("{:<5} {:<20} {:<50} {:<20} {:<10} {:<20}".format(bikeID, '| '+name, '| '+brand, '| '+color,'| '+quantity,'| '+price.replace('\n','')))
        print('--------------------------+--------------------------------------------------+--------------------+----------+--------')
        bikeID+= 1

#this function displays Bikes
def displayBike():
    print("\n\n------------------")
    print("| Display  Bikes |")
    print("------------------\n")
    showBike()
    print('\n')
    options()

#this function purchase bike, print user details and bike details in txt file and subtracts quantity
def purchaseBike():
    print("\n\n----------------------")
    print("|  Purchase  Bikes   |")
    print("----------------------\n")
    name = input("\nEnter the name of the buyer: ")
    address = input("\nEnter the address of the buyer: ")
    contact = input("\nEnter the contact of the buyer: ")
    date = getTime()
    invoiceName = name + getTime().replace(':','').replace('-','') + '.txt'
    buyMore = True
    orderedBike = {}
    while buyMore:
        showBike()
        bike = 0
        while not bike > 0:
            try:
                bike = int(input("\nEnter the id of the bike you want to purchase: "))
                if not bike in range(1,6):
                    print("Add Id of bike that is listed")
            except:
                print("Please enter valid number")

        bikeQ = int(input("\nEnter the total quantity you want to purchase: "))


        if bikeQ > int(_list()[bike - 1][3]):
            print("\nSorry, We do not have enough quantity in our stock. Please try with fewer bikes.\n\n")
        else:

            result = _list()
            result[bike-1][3] = str(int(result[bike-1][3]) - bikeQ)
            #It is same as f2 = open ('bikes.txt'), w.
            with open('bikes.txt', 'w') as f2:
                data = ""
                for i in result:
                    for j in i:
                        data += str(j)+","
                    data = data[:-1]
                f2.write(data)

            orderedBike.update({bike:bikeQ})
            print("\nBike added for purchase.")
            print("\nDo you want to purchase more bikes? Press 1 for Yes and 0 for No\n")
            yesno = int(input(": "))
            if yesno == 0:
                buyMore = False

        with open(invoiceName, 'w') as f:
            f.write('Buyer Name: ' + name + '\nBuyer Address: ' + address + '\nBuyer Contact: ' + contact + '\nPurchase Date: ' + date + '\n\n\nBikes Purchased:\n---------------------------------------------------------\n')

        grandTotal = 0
        for i in orderedBike:
            with open(invoiceName, 'a') as f:
                f.write('Bike Name: ' + result[i-1][0] + '\nBike Color: ' + result[i-1][2] + '\nUnit Price: ' + result[i-1][4] + 'Quantity: ' + str(orderedBike[i]) + '\nTotal Amount: $' + str(int(result[i-1][4].replace('$',''))*orderedBike[i]) + '\n---------------------------------------------------------\n')
            grandTotal = grandTotal + int(result[i-1][4].replace('$',''))*int(orderedBike[i])

        with open(invoiceName, 'a') as f:
            f.write('\nGrand Total: $' + str(grandTotal))

        print('\n\n Your selected bikes were purchased successfully. \n')
        with open(invoiceName, 'r') as f:
            for line in f:
                print(line)

    options()
#this function add stocks, prits Distributor details and bike details in a txt file
def addStock():
    print("\n\n------------------")
    print("|   Add  Stock   |")
    print("------------------\n")
    name = input("\nEnter the name of the Distributor: ")
    address = input("\nEnter the address of the Distributor: ")
    contact = input("\nEnter the contact of the Distributor: ")
    date = getTime()

    stockName = name + getTime().replace(':','').replace('-','') + '.txt'
    addMore = True
    orderedBike = {}
    while addMore:
        showBike()
        bikeDetails = []
        bike = 0
        while not bike > 0:
            try:
                bike = int(input("\nEnter the id of bike you want to add Stock: "))
                if not bike in range(1,6):
                    print("Bike not found")
            except:
                print("Please enter valid number")
        bikeQ = int(input("\nEnter the total quantity you want to add stock: "))
        ship = input("\nEnter the name of the Shipping Company: ")
        shippingCost = input("\nEnter the shipping Cost: ")
        bikeDetails = [bikeQ,ship,shippingCost.replace('$','')]


        result = _list()
        result[bike-1][3] = str(int(result[bike-1][3]) + bikeQ)
        with open('bikes.txt', 'w') as f2:
            data = ""
            for i in result:
                for j in i:
                    data += str(j)+","
                data = data[:-1]
            f2.write(data)

        orderedBike.update({bike:bikeDetails})
        print("\nBike added to the stock.")
        print("\nDo you want to add more bikes? Press 1 for Yes and 0 for No\n")
        yesno = int(input(": "))
        if yesno == 0:
            addMore = False

        with open(stockName, 'w') as f:
            f.write('Distributor Name: ' + name + '\nDistributor Address: ' + address + '\nDistributor Contact' + contact + '\nTransation Date: ' + date + '\n\n\nBikes Added:\n---------------------------------------------------------\n')

        grandTotal = 0
        for i in orderedBike:
            with open(stockName, 'a') as f:
                grandTotal = grandTotal + int(result[i-1][4].replace('$','')) * int(orderedBike[i][0])
                f.write('Bike Name: ' + result[i-1][0])
                f.write('\nBike Color: ' + result[i-1][2])
                f.write('\nUnit Price: ' + result[i-1][4])
                f.write('Quantity: ' + str(orderedBike[i][0]))
                f.write('\nTotal Amount: $' + str(int(result[i-1][4].replace('$',''))*orderedBike[i][0]))
                f.write('\nShipping Company' + orderedBike[i][1])
                f.write('\nShipping Cost: $' + orderedBike[i][2])
                f.write('\n\n---------------------------------------------------------\n\n')

        with open(stockName, 'a') as f:
            f.write('\nGrand Total: $' + str(grandTotal))

        print('\n\n Your selected bikes were added successfully. As below: \n')
        with open(stockName, 'r') as f:
            for i in f:
                print(i)
        #print(orderedBike)

    options()

#This function will add bike to txt file and write Distributor and bike details in txt file
def addBike():
    print("\n\n----------------")
    print("| Add new Bike |")
    print("----------------\n\n")

    bikeName = input("Enter the name of the bike: ")
    bikeBrand = input("Enter the brand of the bike: ")
    bikeColor = input("Enter the color of the bike: ")
    bikeQuantity = 0
    while not bikeQuantity > 0:
        try:
            bikeQuantity = int(input("Enter the quantity of the bike: "))
        except:
            print("\nPlease enter a valid number greater than 0\n")
    bikePrice = input("Enter the price of the bike: ")

    def add(name,brand,color,quantity,price):
        print("\n\nYou're trying to add new bike with following details:\nName: ",name,"\nBrand: ",brand,"\nColor: ",color,"\nQuantity: ",quantity,"\nPrice: ",price)

        confirm = -1
        while not confirm in range(0,2):
            try:
                confirm = int(input("\nDo you wish to continue? Press 1 to confirm 0 to cancel: "))
            except:
                print("\nPlease enter 1 to confirm and 0 to cancel.")

        if confirm == 1:
            #Add to bike code Here
            data = str(name+','+brand+','+color+','+str(quantity)+','+price+'\n')
            #print(data)
            with open('bikes.txt', 'a') as f:
                f.write(data)

                #print('Coming soon')
            print('Your data have been saved\n\n')
            options()

        elif confirm == 0:
            print('Nothing has been saved\n\n')
            options()

        else:
            print('\nInvalid option, Please try again')


    add(bikeName,bikeBrand,bikeColor,bikeQuantity,bikePrice)

    options()
