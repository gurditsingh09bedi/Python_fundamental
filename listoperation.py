list_one = []

list_size = int(input("Enter the size of First list"))
for i in range(list_size):
    first_list_input = input("Enter the First List Values =")
    list_one.append(first_list_input)
print(list_one)


while True:
    print("*****List having many operation few of them are mention below*****")
    print("For Insertion Enter 1 \n For Extend Enter 2 \n For Removal Enter 3 \n For Sorting Enter 4")
    num_in = int(input("Enter your choice ="))
    if num_in == 1:
        list_two = []
        second_list_size = 1
        postion = int(input("Enter the index where would you like to insert in list"))
        for i in range(second_list_size):
            second_list_input = input("Enter the First List Values =")
            list_two.insert(postion,second_list_input)
        print(list_two)
        for i in list_two:
            list_one.append(i)
        print(list_one)
    elif num_in == 2:
        list_two = []
        second_list_size = int(input("Enter the size of Second list"))
        for i in range(second_list_size):
            second_list_input = input("Enter the First List Values =")
            list_two.extend(second_list_input)
        print(list_two)
        for i in list_two:
            list_one.append(i)
        print(list_one)
    elif num_in == 3:
        print("Your input list is =",list_one)
        removal_userinput = input("What would you like to remove from your list =")
        list_one.remove(removal_userinput)
        print(list_one)
    elif num_in == 4:
        print("Your input list is =",list_one)
        list_one.sort()
        print("After Sorting of your list =",list_one)
    else:
        pass
    num_con = input("What would you like to do, Do you want to continue [Yes/No] =")
    if num_con == "no":
        break   


    