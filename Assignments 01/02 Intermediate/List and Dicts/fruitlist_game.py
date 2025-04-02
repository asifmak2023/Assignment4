def main():
    lst = ["apple", "banana", "orange", 1, 5]
    print(f"The list has {len(lst)} elements.")   
    lst.append("mango")
    print(lst)

    lst_value = get_element_at_index(lst, 3)
    print(lst_value)

    # Example usage of the new function
    updated_list = replace_element_at_index(lst, 2, "grape")
    print(updated_list)

def get_element_at_index(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range."
    return lst[index]

def replace_element_at_index(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index out of range."
    lst[index] = new_value
    return lst

if __name__ == "__main__":
    main()
