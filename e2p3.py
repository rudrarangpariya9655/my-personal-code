cart = []

str1="*******"

while True:
    option=int(input("1.Add Item\n2.Update\n3.Remove\n4.Display\n-1.exit\nEnter your chopice :"))
    
    if option==1:
        l=[]
        item=input("Enter Item :")
        quantity=int(input("Enter Quantity :"))
        while quantity<0:
            quantity=int(input("Enter Quantity greterthen 0 :"))
        price=int(input("enter price :"))
        while price<0:
            price=int(input("Enter Price greterthen 0 :"))
        
        l.append(item)
        l.append(quantity)
        l.append(price)
        l.append(price*quantity)

        cart.append(l)

    elif option==2:
        if cart:
            for item in cart:
                print(item[0])

            item=input("\nEnter item from above :")
                
            change=int(input("\n1.Item\n2.quantity\n3.price\n"))
            
            for i in cart:
                if i[0]==item:
                    if change==1:
                        i[0]=input("give item name")
                    elif change==2:
                        i[1]=int(input("Enter quantity :"))
                        i[3]=i[1]*i[2]
                    elif change==3:
                        i[2]=int(input("Enter Price :"))
                        i[3]=i[1]*i[2]
        else:
            print("cart is empty")
    
    elif option==3:
        if cart:
            for item in cart:
                print(item[0])

            item=input("\n\nEnter the Item from above :")
            for i in cart:
                if i[0]==item:
                    cart.remove(i)
                    break
            else:
                print("there is not any item name with :",item)
        else:
            print("cart is empty")
        
    elif option==4:
        if cart:
            count=1
            print(str1*10)
            print("Sr.no".ljust(6),"Item".ljust(20),"Quantity".ljust(10),"Price".ljust(10),"Total".ljust(10))
            print(str1*10)
            for i in cart:
                print(str(count).ljust(6),i[0].ljust(20),str(i[1]).ljust(10),str(i[2]).ljust(10),str(i[3]).ljust(10))
                count+=1
            print(str1*10)
        else:
            print("Cart is empty")

    elif option==-1:
        break