# Billing Stock System

BillingDict = {}

def InputFun():
    while True:
        SKU = int(input("Enter SKU (Unique Number): "))
        ProductName = input("Enter Product Name: ")
        QT = int(input("Enter Product QT: "))
        SinglePrice = int(input("Enter Single Product Price: "))

        BillingDict[SKU] = {"ProductName": ProductName, "QT": QT, "SinglePrice": SinglePrice}

        print("----------------------------------------------")
        AddMore = input("Do you want to add more items? [y/n]: ")
        print("----------------------------------------------")
        
        if AddMore == "Y" or AddMore == "y":
            continue
        elif AddMore == "N" or AddMore == "n":
            AddMoreNo()
            break
        else:
            print("Invalid Input")
            break

def AddMoreNo():
    print("----------------OUTPUT------------------")
    print("-------------SEARCH ITEM-----------------")
    SearchItem = int(input("Enter Product Item From SKU No.: "))
    print("----------------------------------------------")

    # Iterate over the dictionary to find the SKU
    for i in BillingDict:
        if i == SearchItem:
            print(f"Total Cost: {BillingDict[i]['QT'] * BillingDict[i]['SinglePrice']}/-")
            print(f"Product Name: {BillingDict[i]['ProductName']}")
            print(f"QT: {BillingDict[i]['QT']}")
            print(f"Single Price: {BillingDict[i]['SinglePrice']}/-")
            print("----------------------------------------------")
            break
    else:
        print("No such SKU Number present.")

InputFun()
