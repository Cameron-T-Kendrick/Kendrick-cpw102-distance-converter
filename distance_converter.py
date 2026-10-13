def convert_miles_to_feet(miles):
    return miles * 5280

def convert_inches_to_miles_feet_inches(inches_one):
    new_miles = inches_one // 63360
    remaining = inches_one % 63360

    new_feet = remaining // 12
    new_inches = remaining % 12
    return new_miles, new_feet, new_inches

def main():
    print("Enter your mesurements in Miles, Feet, and inches below:  ")
    miles = int(input("Miles: "))
    feet = int(input("Feet: "))
    inches = int (input("Inches: "))
    
    total_inches = (convert_miles_to_feet(miles) * 12) + (12 * feet) + inches
    
    print(f"{miles} miles, {feet} feet, and {inches} inches is {total_inches}")
    print("Now we will convert your inches to miles, feet, and inches!")


    inches_one = int(input("Inches: ")) 
    new_miles, new_feet, new_inches = convert_inches_to_miles_feet_inches(inches_one)

    print(f"Inputed Inches: {inches_one}")
    print(f"{inches_one} inches is {new_miles} miles, {new_feet} feet, and {new_inches} Inches." )


main()