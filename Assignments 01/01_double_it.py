def main():
    
    curr_value = 0
    while(curr_value<=100):
        num = int(input("Enter a number and I will double it! :"))
        curr_value = num * 2
        print(f"Number doubled is : {curr_value}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()