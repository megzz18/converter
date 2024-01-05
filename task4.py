def main():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Feet")
    print("4. Feet to Meters")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        kilometers = float(input("Enter distance in kilometers: "))
        miles = kilometers * 0.621371
        print(f"{kilometers} kilometers is equal to {miles} miles.")
    elif choice == 2:
        miles = float(input("Enter distance in miles: "))
        kilometers = miles / 0.621371
        print(f"{miles} miles is equal to {kilometers} kilometers.")
    elif choice == 3:
        meters = float(input("Enter distance in meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is equal to {feet} feet.")
    elif choice == 4:
        feet = float(input("Enter distance in feet: "))
        meters = feet / 3.28084
        print(f"{feet} feet is equal to {meters} meters.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
