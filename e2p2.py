students = []

str1 = "******"

while True:

    option = int(input("1.Add student detail\n2.Update\n3.Delete\n4.Display\n-1.Exit: "))
    print("\n", str1 * 5, "\n")

    if option == 1:
        li = []

        name = input("Enter name : ")
        sub_name = input("Enter Subject name : ")

        mark = int(input("Enter mark : "))
        while mark > 100 or mark < 0:
            mark = int(input("Enter valid mark (0-100): "))

        li.append(name)
        li.append(sub_name)
        li.append(mark)

        students.append(li)

        print("\n", str1 * 5, "\n")

    elif option == 2:
        if not students:
            print("List is empty")
            print("\n", str1 * 5, "\n")

        else:
            op = int(input("Enter what you want to change\n1.Subject name\n2.Marks\n: "))
            name = input("Enter student name to update: ")

            if op == 1 or op == 2:
                for student in students:
                    if student[0].lower() == name.lower():

                        if op == 1:
                            student[1] = input("Enter new subject name: ")
                            break

                        elif op == 2:
                            mark = int(input("Enter new marks: "))
                            while mark > 100 or mark < 0:
                                mark = int(input("Enter valid mark (0-100): "))
                            student[2] = mark
                            break
                else:
                    print("There is no student with name:", name)
                    print("\n", str1 * 5, "\n")
            else:
                print("Give valid option")
                print("\n", str1 * 5, "\n")

    elif option == 3:
        if not students:
            print("List is empty")
            print("\n", str1 * 5, "\n")

        else:
            name = input("Which student you want to delete: ")

            for student in students:
                if student[0].lower() == name.lower():
                    students.remove(student)
                    print("\n", str1 * 5, "\n")
                    break
            else:
                print("There is no student with name:", name)
                print("\n", str1 * 5, "\n")

    elif option == 4:
        if students:
            count = 1
            print(str1 * 10)
            print("Sr.no".ljust(6), "Student name".ljust(20),
                  "Subject Name".ljust(20), "Marks".ljust(10))
            print(str1 * 10)

            for i in students:
                print(str(count).ljust(6),
                      i[0].ljust(20),
                      i[1].ljust(20),
                      str(i[2]).ljust(10))
                count += 1

            print(str1 * 10)

        else:
            print("List is empty")
            print("\n", str1 * 5, "\n")

    elif option == -1:
        print("\n", str1 * 5, "\n")
        break

    else:
        print("Invalid option")
        print("\n", str1 * 5, "\n")