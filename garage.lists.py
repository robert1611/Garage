class ParkingGarage:
    # tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # currentTicket = {'paid': False}

    def __init__(self,tickets, parkingSpaces, currentTicket):
        self.parkingSpaces = parkingSpaces
        self.tickets = tickets
        self.currentTicket = currentTicket

    # takeTicket will output a ticket upon request as long as currentTicket <= 10.  This will decrement both parkingSpaces an currentTicket by 1
    def takeTicket(self):
        if self.tickets != [] and self.parkingSpaces!= [] :
            print("you can enter")
            self.parkingSpaces.pop()
            self.tickets.pop()

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
            print("Your ticket has been paid.  Please exit within 15 minutes")
            self.currentTicket["paid"] = True
        else:
            # The print statement is nest within the if statement, so it should execute
            print("Your ticket has NOT been paid.")

    def leaveGarage(self):
        if self.currentTicket["paid"] != True:
            print("Please pay first!!!")
            return
        if len(self.parkingSpaces)<10 and len(self.tickets)<10:
            self.parkingSpaces.append(len(self.parkingSpaces)+1)
            self.tickets.append(len(self.tickets) + 1)
            print("you can leave")
            self.currentTicket["paid"] = False
        else:
            print("Are you certain you're at the garage? We show no cars in the system !!!")

        # to remove
        print(self.tickets)
        print(self.parkingSpaces)



def run():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    currentTicket = {'paid': False}
    parkingGarage = ParkingGarage(tickets, parkingSpaces, currentTicket)
    while True:
        response = input("What do you want to enter, pay, leave or quit?  ")
        if (response.lower() == 'enter'):
            parkingGarage.takeTicket()
        elif (response.lower() == 'pay'):
            parkingGarage.payForParking()
        elif (response.lower() == 'leave'):
            parkingGarage.leaveGarage()
        elif(response.lower() == "quit"):
            break


run()