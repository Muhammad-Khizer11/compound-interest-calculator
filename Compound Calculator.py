while True:

    principle = 0
    rate = 0
    time = 0

    while True:
        principle = float(input("Enter your principle amount: "))
        if principle < 0:
            print("Invalid input, please try again")
        else:
            break
    while True:
        rate = float(input("Enter your interest rate: "))
        if rate < 0:
            print("Invalid input, please try again")
        else:
            break

    while True:
        time = float(input("Enter your time period in Years: "))
        if time < 0:
            print("Invalid input, please try again")
        else:
            break
    total = principle * pow((1 + rate / 100), time)

    print(f"Balance after {time} year is £{total:.2f}")
    again = input("Do you want to start again (Y/N): ").upper()
    if again == "N":
        print("Goodbye")
        break


