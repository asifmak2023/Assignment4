def main():
    lst = ["apple", "banana", "orange", 1, 5]
    print(f"The list has {len(lst)} elements.")   
    lst.append("mango")
    print(lst)

    while True:
        print("\nSelect an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter the index to access: "))
            result = get_element_at_index(lst, index)
            print(f"Result: {result}")

        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            updated_list = replace_element_at_index(lst, index, new_value)
            print(f"Updated list: {updated_list}")

        elif choice == '3':
            start_index = int(input("Enter the start index: "))
            end_index = int(input("Enter the end index: "))
            sliced_list = slice_list(lst, start_index, end_index)
            print(f"Sliced list: {sliced_list}")

        elif choice == '4':
            print("Exiting the game.")
            break

        else:
            print("Invalid choice. Please try again.")

def get_element_at_index(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range."
    return lst[index]

def replace_element_at_index(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index out of range."
    lst[index] = new_value
    return lst

def slice_list(lst, start_index, end_index):
    # Handle out of range indices
    if start_index < 0 or end_index > len(lst) or start_index >= end_index:
        return "Invalid index range."
    
    return lst[start_index:end_index]

if __name__ == "__main__":
    main()
