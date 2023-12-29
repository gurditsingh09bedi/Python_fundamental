list_one = []

list_size = int(input("Enter the size of First set"))
for i in range(list_size):
    first_list_input = input("Enter the First List Values =")
    list_one.append(first_list_input)
set_one = set(list_one)
print(set_one)
print(type(set_one))

list_secon = []

second_list_size = int(input("Enter the size of Second set"))
for i in range(second_list_size):
    second_list_input = input("Enter the Second List Values =")
    list_one.append(first_list_input)
set_two = set(list_one)
print(set_two)
print(type(set_two))


tuple_tree = set_one + set_two
print(tuple_tree)
print(type(tuple_tree))