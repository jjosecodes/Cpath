


def is_subsequence(lst, sequence):
    index = 0
    for num in lst:
        if index < len(sequence) and num == sequence[index]:
            index += 1
    return index == len(sequence)

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))

def create_dictionary(keys, values):
    Keyvalue = {}
    for i in range(len(keys)):
        Keyvalue[keys[i]] = values[i]
    return Keyvalue

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
#print(result = create_dictionary(keys, values))


def print_pair(dictionary, target):
    if target in dictionary:
        print(f"Key: {target} ")
        print(f"Value: {dictionary[target]}")
    else:
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
#print_pair(dictionary, "patrick")
#print_pair(dictionary, "plankton")
#print_pair(dictionary, "spongebob")

def keys_v_values(dictionary):
    sum_of_keys = 0
    sum_of_values = 0
    for k, v in dictionary.items():
        sum_of_keys += k
        sum_of_values += v

    if sum_of_keys > sum_of_values:
        return "keys"
    elif sum_of_values > sum_of_keys:
        return "values"
    else:
        return "balanced"


dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
#print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
#print(greater_sum)



def restock_inventory(current_inventory, restock_list):
    for i in restock_list:
        if i in current_inventory:
            current_inventory[i] += restock_list[i]
        else:
            current_inventory[i] = restock_list[i]
    return current_inventory


current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

updated_inventory = restock_inventory(current_inventory, restock_list)
print(updated_inventory)
