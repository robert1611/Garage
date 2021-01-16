class ParkingGarage:
    """# parkingSpaces = 0
    # tickets = 10
    # currentTicket = {
    #     "paid": False,
    # }"""

    def __init__(self):

        self.parkingSpaces = 0
        self.tickets = 10
        self.currentTicket = {
            "paid": False,
        }

    # takeTicket will output a ticket upon request as long as currentTicket <= 10.
    def takeTicket(self):
        if self.parkingSpaces < 10 and self.tickets > 0:
            print("you can enter")
            self.parkingSpaces = self.parkingSpaces + 1
            self.tickets = self.tickets - 1

            # to remove
            print(self.tickets)
            print(self.parkingSpaces)

        else:
            print("We're sorry. No Parking available")

            # to remove
            print(self.tickets)
            print(self.parkingSpaces)

    # Display an input that waits for an amount from the user and stores it in a variable
    def payForParking(self):
        payment = input("Enter the payment: ")
        if payment != "":
            # The print statement is nest within the if statement, so it should execute
            print("Have a nice day")
            self.currentTicket["paid"] = True
        else:
            # The print statement is nest within the if statement, so it should execute
            print("Your ticket has NOT been paid.")

    def leaveGarage(self):
        if self.currentTicket["paid"] != True:
            print("Please pay first!!!")
            return

        if self.parkingSpaces > 0:
            self.parkingSpaces = self.parkingSpaces - 1
            self.tickets = self.tickets + 1
            print("you can leave")
            self.currentTicket["paid"] = False
        else:
            print("Are you sure you're parked here.  The garage is empty !!!")

#make sure this is outside of the class loop in order to run
def run():
    parkingGarage = ParkingGarage()
    while True:
        response = input("What do you want to enter, pay or leave?  ")
        if (response.lower() == 'enter'):
            parkingGarage.takeTicket()
        elif (response.lower() == 'pay'):
            parkingGarage.payForParking()
        elif (response.lower() == 'leave'):
            parkingGarage.leaveGarage()
        else:
            ("Invalid response")


run()