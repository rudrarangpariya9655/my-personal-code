cart = []

str1 = "*******"

while True:

    option = int(input("1.Add Item\n2.Update\n3.Remove\n4.Display\n-1.Exit\nEnter your choice: "))
    print("\n", str1 * 5, "\n")

    if option == 1:
        l = []

        item = input("Enter Item : ")

        quantity = int(input("Enter Quantity : "))
        while quantity <= 0:
            quantity = int(input("Enter valid Quantity (>0) : "))

        price = int(input("Enter Price : "))
        while price <= 0:
            price = int(input("Enter valid Price (>0) : "))

        total = quantity * price

        l.append(item)
        l.append(quantity)
        l.append(price)
        l.append(total)

        cart.append(l)

        print("\n", str1 * 5, "\n")

    elif option == 2:
        if not cart:
            print("Cart is empty")
            print("\n", str1 * 5, "\n")

        else:
            print("Items in cart:")
            for i in cart:
                print(i[0])

            item_name = input("\nEnter item from above: ")

            change = int(input("\n1.Item Name\n2.Quantity\n3.Price\n: "))

            if change in (1, 2, 3):
                for i in cart:
                    if i[0].lower() == item_name.lower():

                        if change == 1:
                            i[0] = input("Enter new item name: ")

                        elif change == 2:
                            quantity = int(input("Enter new quantity: "))
                            while quantity <= 0:
                                quantity = int(input("Enter valid Quantity (>0): "))
                            i[1] = quantity
                            i[3] = i[1] * i[2]

                        elif change == 3:
                            price = int(input("Enter new price: "))
                            while price <= 0:
                                price = int(input("Enter valid Price (>0): "))
                            i[2] = price
                            i[3] = i[1] * i[2]

                        print("\n", str1 * 5, "\n")
                        break
                else:
                    print("There is no item with name:", item_name)
                    print("\n", str1 * 5, "\n")
            else:
                print("Invalid option")
                print("\n", str1 * 5, "\n")

    elif option == 3:
        if not cart:
            print("Cart is empty")
            print("\n", str1 * 5, "\n")

        else:
            print("Items in cart:")
            for i in cart:
                print(i[0])

            item_name = input("\nEnter item from above: ")

            for i in cart:
                if i[0].lower() == item_name.lower():
                    cart.remove(i)
                    print("\n", str1 * 5, "\n")
                    break
            else:
                print("There is no item with name:", item_name)
                print("\n", str1 * 5, "\n")

    elif option == 4:
        if cart:
            count = 1
            grand_total = 0

            print(str1 * 10)
            print("Sr.no".ljust(6),
                  "Item".ljust(20),
                  "Quantity".ljust(10),
                  "Price".ljust(10),
                  "Total".ljust(10))
            print(str1 * 10)

            for i in cart:
                print(str(count).ljust(6),
                      i[0].ljust(20),
                      str(i[1]).ljust(10),
                      str(i[2]).ljust(10),
                      str(i[3]).ljust(10))
                grand_total += i[3]
                count += 1

            print(str1 * 10)
            print("Grand Total:".ljust(46), grand_total)
            print(str1 * 10)

        else:
            print("Cart is empty")
            print("\n", str1 * 5, "\n")

    elif option == -1:
        print("\n", str1 * 5, "\n")
        break

    else:
        print("Invalid option")
        print("\n", str1 * 5, "\n")
