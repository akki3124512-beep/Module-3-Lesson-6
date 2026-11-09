try:

    car = float(input("Enter the cost of the car rental: "))
    plane = float(input("Enter the cost of the plane ride: "))
    hotel = float(input("Cost of hotel room per day: "))
    days = float(input("How many days in hotel: "))

    def total(a,b,c,d):
        return a+b+(c*d)

    print("The total of your trip expenditure is: ", total(car,plane,hotel,days))

except:
    print("Enter a valid number in digit form.")