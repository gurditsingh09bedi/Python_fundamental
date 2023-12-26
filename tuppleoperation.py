list_one = []

list_size = int(input("Enter the size of First tuple"))
for i in range(list_size):
    first_list_input = input("Enter the First List Values =")
    list_one.append(first_list_input)
tup = tuple(list_one)
print(tup)
print(type(tup))

list_secon = []

second_list_size = int(input("Enter the size of Second tuple"))
for i in range(second_list_size):
    second_list_input = input("Enter the Second List Values =")
    list_one.append(first_list_input)
tup2 = tuple(list_one)
print(tup)
print(type(tup))


tuple_tree = tup + tup2
print(tuple_tree)
print(type(tuple_tree))