def fact_solve(num):
    num = 1
    for i in range(1, pos_int + 1):
        num *= i
        print("The factorial of %s is %s. " % (i, num))
        
cont = True

while cont == True:
    pos_int = input("Please enter a positive integer: ")
    if pos_int.isdigit():
        pos_int = int(pos_int)
        if pos_int > 0:
            option = input("How would you like to solve the factorial?  \n"
                           "Option '1': Sequential programming.  \n"
                           "Option '2': Recursive programming.  \n"
                           "Please enter either '1' or '2': ")
            if option == '1':
                num = 1
                for i in range(1, pos_int + 1):
                    num *= i
                print("The factorial of %s is %s. " % (i, num))
                cont = False
            elif option == '2':
                fact_solve(pos_int)
                cont = False
            else:
                print("That is not an option! ")
        elif pos_int == 0:
            print("The factorial of 0 is 1! ")
        else:
            print("Please enter a positive integer! ")
    else:
        print("Please enter a positive integer! ")
