def main():
    print("This program converts temperature from degree fahrenheit to degree celsius :)")
    
    deg_fah = int(input("Enter Degree Fahrenheit Temperature: "))
    deg_cel =  (deg_fah - 32) * 5.0/9.0
    
    print(f"Temperature in Deg Celsius = {deg_cel}F")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()