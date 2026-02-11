from ast import Continue


students=[]

str1="-------"


while True:

    option=int(input("1.Add student detail\n2.Update\n3.Delete\n4.Display\n-1.exit: "))
    print("\n",str1*5,"\n")
    
    if option==1:
        li=[]

        name=input("Enter name : ")
        attendance=input("Enter  attendance P/A: ").upper()
        while attendance!="P" and attendance!="A":
            attendance=input("Enter valid attendance P/A: ").upper()
        date=input("Enter date : ")
        while len(date)!=10:
            date=input("Enter valid date : ")         

        li.append(name)
        li.append(attendance)
        li.append(date)

        students.append(li)
        
        print("\n",str1*5,"\n")
    
    elif option==2:
        if not students:
            print("List is empty")
            print("\n",str1*5,"\n")
            
        else:
            op=int(input("Enter What you want to change \n1.Name\n2.Attendance : "))
            name=input("In which student name you want to update : ")
            if op==2 or op==1:
                for student in students:
                    if (student[0].lower())==(name.lower()):
                        if op==1:
                            student[0]=input("enter name to update : ")
                            break
                        elif op==2:
                            attendance=input("Enter  attendance P/A: ").upper()
                            while not(attendance=="P" or attendance=="A"):
                                attendance=input("Enter  attendance P/A: ").upper()
                            student[1]=attendance
                            print("\n",str1*5,"\n")
                            break
                    
                else:
                    print("there is not any name")
                    print("\n",str1*5,"\n")
            else:
                print("give valid option")
                print("\n",str1*5,"\n")


    elif option == 3:
            
        if not students:
            print("List is empty")
            print("\n",str1*5,"\n")
        else:
            name=input("which student you want to delete : ")
            for student in students:
                if (student[0].lower())==(name.lower()):
                    students.remove(student) 
                    print("\n",str1*5,"\n")
                    break
                
            else:
                print("there is not any name with :",name)
                print("\n",str1*5,"\n")
                

    elif option==4:
        
        if students:
            count=1
            print(str1*10)
            print("Sr.no".ljust(10),"Student name".ljust(20),"Attendance".ljust(10),"Date".ljust(10))
            print(str1*10)
            for i in students:
                print(str(count).ljust(10),i[0].ljust(20),str(i[1]).ljust(10),(i[2]).ljust(10))
                count+=1
            print(str1*10)
        else:
            print("List is empty")
            print("\n",str1*5,"\n")
            
    elif option==-1:
        print("\n",str1*5,"\n")
        break
        