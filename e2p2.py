students=[]

str1="******"


while True:

    option=int(input("1.Add student detail\n2.Update\n3.Delete\n4.Display : "))
    if option==1:
        li=[]

        name=input("Enter name : ")
        sub_name=input("Enter Subject name : ")
        mark=int(input("Enter mark : "))
        while mark>100 or mark<0:
            mark=int(input("Enter  0<mark<100: "))

        li.append(name)
        li.append(sub_name)
        li.append(mark)
        students.append(li)
    
    elif option==2:
        if students:
            op=int(input("enter Choice to update \n1.Subject name\n2.Marks\n:"))
            if op==1:
                stu_name=input("Enter which student subject name you want to update :")
                sub_name=input("Enter Subject name to change :")
                for student in students:
                    if student[0]==stu_name:
                        student[1]=sub_name
                        break
                else:
                    print("ther is not any name with :",stu_name)
            if op==2:
                stu_name=input("Enter which student subject name you want to update :")
                marks=input("Enter Marks to change :")
                while mark>100 or mark<0:
                    mark=int(input("Enter  0<mark<100: "))
                for student in students:
                    if student[0]==stu_name:
                        student[2]=marks
                        break
                else:
                    print("ther is not any name with :",stu_name)
        else:
            print("list is empty")

    elif option==3:
        if students:
                name=input("Enter name to delete :")
                for student in students:
                    if student[0]==name:
                        students.remove(student)
                        break
                else:
                    print("there is not any name with :",name)
        else:
            print("list is empty")


    elif option==4:
        if students:
            count=1
            print(str1*10)
            print("Sr.no".ljust(6),"Student name".ljust(20),"Subject Name".ljust(20),"Marks".ljust(10))
            print(str1*10)
            for i in students:
                print(str(count).ljust(6),i[0].ljust(20),i[1].ljust(20),str(i[2]).ljust(10))
                count+=1
            print(str1*10)
        else:
            print("List is empty")
    elif option==-1:
        break