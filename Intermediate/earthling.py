def main():
    earthling = int(input("Enter mass of an object on Earth! :"))
    
    planet = input("Enter the name of a planet (e.g., Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")
    
    # Define gravitational constants for each planet
    gravity_constants = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    # Calculate weight on the specified planet
    if planet in gravity_constants:
        weight_on_planet = earthling * gravity_constants[planet]
        print(f"Weight on {planet} is: {weight_on_planet:.2f} kg")
    else:
        print("Invalid planet name. Please enter a valid planet.")

if __name__ == '__main__':
    main() 