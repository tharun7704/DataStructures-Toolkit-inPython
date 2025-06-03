def string_operations(my_str):
    while True:
        print('''\n**STRING IMPLEMENTATION*******************
        1. About Strings
        2. Print String
        3. Concatenate String
        4. Length of String
        5. Access Character using index in the string
        6. Slice String
        7. String Repetition
        8. Minimum and Maximum characters
        9. Uppercase and Lowercase
        10.Check for Substring
        11.Count Occurrences
        12.Replace Substring
        13.Capitalize first char in the string 
        14. Return to Main Menu''')
        ch = int(input("Enter your choice (1-14): "))
        if ch == 1:
            print('''\nDEF: A string is a collection of characters enclosed within single or double quotes 
It is a primitive data structure in python\n''')
        elif ch == 2:
            print("String:", my_str)
        elif ch == 3:
            str1 = input("Enter another string to concatenate: ")
            str2 = my_str + " " + str1
            print("Concatenated String:", str2)
        elif ch == 4:
            length = len(my_str)
            print("Length of String:", length)
        elif ch == 5:
            index = int(input("Enter an index to access from the string: "))
            try:
                char = my_str[index]
                print("Accessed Character:", char)
            except IndexError:
                print("Index out of range!")
        elif ch == 6:
            start_index = int(input("Enter the start index for slicing: "))
            end_index = int(input("Enter the end index for slicing: "))
            sliced = my_str[start_index:end_index]
            print("Sliced String:", sliced)
        elif ch == 7:
            repeat = int(input("Enter the repetition factor: "))
            str5 = my_str * repeat
            print("Repeated String:", str5)
        elif ch == 8:
            print("Minimum string character is :", min(my_str))
            print("Maximum string character is :", max(my_str))
        elif ch == 9:
            upper = my_str.upper()
            lower = my_str.lower()
            print("Uppercase String:", upper)
            print("Lowercase String:", lower)
        elif ch == 10:
            sub_str = input("Enter a substring to check: ")
            result = sub_str in my_str
            print("Contains Substring (True/False):", result)
        elif ch == 11:
            char = input("Enter a character/string to count occurrences: ")
            res = my_str.count(char)
            print("Count of {}: {}".format(char, res))
        elif ch == 12:
            old = input("Enter the substring to replace: ")
            new = input("Enter the new substring: ")
            replaced = my_str.replace(old, new)
            print("Replaced String:", replaced)
        elif ch == 13:
            print("After Capitalize: ",my_str.capitalize())
        elif ch == 14:
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 14: ")
def list_operations(my_list):
    while True:
        print("""\n***************** LIST IMPLEMENTATION ***************     
        1. About lists
        2. Print your input List
        3. Append an element 
        4. Extend List
        5. Insert Element into the list
        6. Remove Element from the list
        7. Pop Element
        8. Get index of an Element
        9. Count Occurrences of an element in the list
        10.Sort List
        11.Reverse the List
        12.Concatenate two lists
        13.Get length of the list
        14.Get Minimum and Maximum element in the list 
        15.Clear list
        16.Return to Main Menu""")
        ch1 = int(input("Enter your choice (1-16): "))
        if ch1 == 1:
            print('''DEF: A list is built in mutable,ordered,heterogenious,sequence of elements
            syntax:
                   <list_name>= []
                   <list_name>= list()''')
        elif ch1 == 2:
            print("Input List:", my_list)
        elif ch1 == 3:
            x = input("Enter an element to append to the list: ")
            my_list.append(x)
            print("After Append:", my_list)
        elif ch1 == 4:
            y = input("Enter elements to extend the list (space seperated): ").split()
            my_list.extend(y)
            print("After Extend:", my_list)
        elif ch1 ==5:
            index = int(input("Enter an index to insert the element: "))
            in_element = input("Enter an element to insert into the list: ")
            my_list.insert(index, in_element)
            print("After Insert:", my_list)
        elif ch1 == 6:
            x = input("Enter an element to remove from the list: ")
            try:
                my_list.remove(x)
                print("After Remove:", my_list)
            except ValueError:
                print("Element not found in list!")
        elif ch1 == 7:
            index = int(input("Enter an index to pop from the list: "))
            try:
                pop_element = my_list.pop(index)
                print("Popped Element:", pop_element)
                print("After Pop:", my_list)
            except IndexError:
                print("Index out of range!")
        elif ch1 == 8:
            x = input("Enter an element to find its index: ")
            try:
                index = my_list.index(x)
                print("Index of {}: {}".format(x, index))
            except ValueError:
                print("{} not found in list!".format(x))
        elif ch1 == 9:
            element_to_count = input("Enter an element to count its occurrences in the list : ")
            count = my_list.count(element_to_count)
            print("Count of {}: {}".format(element_to_count, count))
        elif ch1 == 10:
            my_list.sort()
            print("Sorted List:", my_list)
        elif ch1 == 11:
            my_list.reverse()
            print("Reversed List:", my_list)
        elif ch1 == 12 :
            list2 = list(input("Enter another list (space seperated ) :"))
            print("After Concatenation :",my_list+list2)
        elif ch1 == 13:
            print("Length of the list is :",len(my_list))
        elif ch1 == 14:
            print("Minimum Element is : ",min(my_list))
            print("Maximum element is : ",max(my_list))
        elif ch1 == 15:
            my_list.clear()
            print("List Cleared.")
        elif ch1 == 16:
            print("Returning to Main Menu.\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 16 : ")


def tuple_operations(my_tuple):
    while True:
        print('''\n*TUPLE IMPLEMENTATION*********************
        1. About Tuple
        2. Print your input Tuple
        3. Access Element in the tuple with index
        4. Concatenate Tuples
        5. Count of an element in the tuple
        6. Get index of an element in the tuple
        7. Return to Main Menu''')
        ch = int(input("Enter your choice (1-7): "))
        if ch == 1:
            print('''DEF :A tuple is a built in immutable,oredered,heterogenious sequence of elements 
                  syntax :
                          <tuple_name> = tuple([elements])
                          <tuple_name> = (elements) ''')
        elif ch == 2:
            print("Tuple:", my_tuple)
        elif ch == 3:
            index_to_access = int(input("Enter an index to access from the tuple: "))
            try:
                accessed_element = my_tuple[index_to_access]
                print("Accessed Element:", accessed_element)
            except IndexError:
                print("Index out of range!")
        elif ch == 4:
            another_tuple = tuple(input("Enter elements for another tuple (space seperated): ").split())
            concate = my_tuple + another_tuple
            print("Concatenated Tuple:", concate)
        elif ch == 5:
            x = input("Enter an element to count : ")
            print(f"Count of {x} in tuple is : ",my_tuple.count(x))
        elif ch == 6:
            x = input("Enter an element to know its index : ")
            print(f"Index of {x} in the tuple is :",my_tuple.index(x))
        elif ch == 7:
            print("Returning to the Main Menu.\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7:")


def set_operations(my_set):
    while True:
        print('''\n*SET IMPLEMENTATION**********************
        1. About sets
        2. Print your input Set
        3. Add Element
        4. Remove Element
        5. Update another set of elements to your set
        6. union of sets
        7. Intersection of sets
        8. Difference of sets  
        9. Symmetric difference of sets 
        10. Clear Set
        11.Return to Main Menu")''')
        choice = int(input("Enter your choice (1-11): "))
        if choice == 1:
            print('''DEF: A Set is a built in unordered collection of unique elements
            syntax:
                   <set_name> = set()
                   <set_name> = {element 1 ,element 2,...........} ''')
        elif choice == 2:
            print("Set:", my_set)
        elif choice == 3:
            y = input("Enter an element to add to the set: ")
            my_set.add(y)
            print("After Adding Element:", my_set)
        elif choice == 4:
            x = input("Enter an element to remove from the set: ")
            try:
                my_set.remove(x)
                print("After Removing Element:", my_set)
            except KeyError:
                print("Element not found in set!")
        elif choice == 5:
            set2 = set(input("Enter another set of elements(space seperated) :").split())
            my_set.update(set2)
            print("After Update :",my_set)
        elif choice == 6:
            set2 = set(input("Enter another set of elements(space seperated) :").split())
            result = my_set.union(set2) # my_set | set2
            print("After union : ",result)
        elif choice == 7:
            set2 = set(input("Enter another set of elements(space seperated) :").split())
            result = my_set.intersection(set2) # my_set & set2
            print("After Intersection :",result)
        elif choice == 8:
            set2 = set(input("Enter another set of elements(space seperated) :").split())
            result = my_set.difference(set2) # my_set - set2
            print("After Differene :",result)
        elif choice == 9:
            set2 = set(input("Enter another set of elements(space seperated) :").split())
            result = my_set.symmetric_difference(set2)
            print("After Symmetrical Differnce :",result)
        elif choice == 10:
            my_set.clear()
            print("Set Cleared.")
        elif choice == 11:
            print("Returning to Main Menu.\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11 : ")

def dict_operations(my_dict):
    while True:
        print('''\n*DICTIONARY IMPLEMENTATION*********************
        1. About dictionaries
        2. Print your input Dictionary
        3. Access Value using key
        4. Add/Replace Key-Value Pair
        5. Remove an item using key
        6. Get list of keys , values
        7. Get tuple of items (key,value) pairs
        8. Get length of dictionary
        9. Clear Dictionary
        10.Return to Main Menu''')

        choice = int(input("Enter your choice (1-10): "))
        if choice == 1:
            print('''DEF: A Dictionary is a collection of key value pair of elements which is mutable and allows heterogenious type of data
            syntax :
                    <dictionary_name> = {}
                    <dictionary_name> = { key1:value1 , key2:value2 , .....keyn: valuen}''')
        elif choice == 2:
            print("Dictionary:", my_dict)
        elif choice == 3:
            key = input("Enter a key to access from the dictionary: ")
            try:
                print("Value:", my_dict.get(key))
            except KeyError:
                print("Key not found in dictionary!")
        elif choice == 4:
            new_key = input("Enter a new key to add to the dictionary: ")
            new_val = input("Enter the corresponding value: ")
            my_dict[new_key] = new_val
            print("After Adding Key-Value Pair:", my_dict)
        elif choice == 5:
            remove = input("Enter a key to remove from the dictionary: ")
            try:
                del my_dict[remove]
                print("After Removing Key:", my_dict)
            except KeyError:
                print("Key not found in dictionary!")
        elif choice == 6:
            print("Keys : ",my_dict.keys())
            print("Values :",my_dict.values())
        elif choice == 7:
            print("Items :",my_dict.items())
        elif choice == 8:
            print("Length : ",len(my_dict))
        elif choice == 9:
            my_dict.clear()
            print("Dictionary Cleared.")
        elif choice == 10:
            print("Returning to Main Menu.\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10: ")

print("******************** IMPLEMENTATION OF BASIC DATASTRUCTURES ******************************")
print("------------------------------------------------------------------------------------------")
while True:
    print('''****************** MAIN MENU ************************
    1. String Implementation
    2. List Implementation
    3. Tuple Implementation
    4. Set Implementation
    5. Dictionary Implentation 
    6. Exit the program ''')
    choice = int(input("Enter your choice (1-6): "))
    if choice == 1:
        str = input("Enter a string :")
        string_operations(str)
    elif choice == 2:
        my_list = list(input("Enter values for List (space-separated): ").split())
        list_operations(my_list)
    elif choice == 3:
        my_tuple = tuple(input("Enter values for Tuple (comma-separated): ").split(','))
        tuple_operations(my_tuple)
    elif choice == 4:
        my_set = set(input("Enter values for Set (space-separated): ").split())
        set_operations(my_set)
    elif choice == 5:
        my_dict= {}
        while True:
            key = input("Enter key for Dictionary (0 to stop): ")
            if key.lower() == '0':
                break
            value = input(f"Enter value for key '{key}': ")
            my_dict[key] = value
        dict_operations(my_dict)
    elif choice ==6:
        print("\nExiting the program !")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5: ")