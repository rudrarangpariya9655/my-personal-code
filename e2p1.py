from ast import Continue


students=[]

str1="*****"


while True:

    option=int(input("1.Add student detail\n2.Update\n3.Delete\n4.Display\n-1.exit: "))
    if option==1:
        li=[]

        name=input("Enter name : ")
        attendance=int(input("Enter  attendance : "))
        while attendance>100 or attendance<0:
            attendance=int(input("Enter  0<attendance<100: "))
        date=input("Enter date : ")

        li.append(name)
        li.append(attendance)
        li.append(date)

        students.append(li)
    
    elif option==2:
        if not students:
            print("List is empty")
            
        op=int(input("Enter What you want to change \n1.Name\n2.Attendance : "))
        name=input("In which student name you want to update : ")
        if op==2 or op==1:
            for student in students:
                if student[0]==name:
                    if op==1:
                        student[0]=input("enter name to update : ")
                        break
                    elif op==2:
                        student[1]=int(input("enter attedance to update : "))
                        break
            else:
                 print("there is not any name")
        else:
             print("give valid option")


    elif option == 3:
            
        if not students:
            print("List is empty")
        else:
            name=input("which student you want to delete : ")
            for student in students:
                if student[0]==name:
                    students.remove(student) 
                    break
            else:
                print("there is not any name with :",name)

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

    elif option==-1:
        break