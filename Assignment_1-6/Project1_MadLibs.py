def madlib():
    # Get user inputs
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    
    # Create the story
    story = f"""
    One day, {name} decided to visit {place}. On the way, {name} saw a {adjective} {animal} 
    eating {food}. Surprised, {name} decided to {verb} towards it. 
    What a strange but fun day!
    """
    
    # Print the story
    print("\nHere is your Mad Lib story:\n")
    print(story)

# Run the Mad Lib game
if __name__ == "__main__":
    madlib()
