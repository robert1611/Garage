#Class: ParkingGarage

#overall the logic seems sloppy.  Why would you have a ticket AND a current 

class ParkingGarage:
    def __init__(self, amountTickets):
        self.amountTickets = amountTickets
        self.tickets = [False] * amountTickets   # False = Available, True = Not Available
        self.parkingSpaces = [False] * amountTickets # False = Available, True = Not Available
        self.currentTicket = {}   #dictionary for a current log for who pays, enters, leaves
        for i in range(amountTickets):
            self.currentTicket[i] = False
    
    # takeTicket will output a ticket upon request as long as currentTicket <= 10.  This will decrement both parkingSpaces an currentTicket by 1
    def takeTicket(self):
        input("Press enter to take a ticket")
        spots_available = 0
        for ticket in self.tickets:
            if ticket == False:
                spots_available = spots_available + 1
        if spots_available > 0:
            #(1) decrement ticket and (2) decrement parking space
            for ticket_number in range(self.amountTickets):
                if self.tickets[ticket_number] == False:
                    self.tickets[ticket_number] = True
                    self.parkingSpaces[ticket_number] = True
                    break
            return "Welcome."
        else:
            return "We're sorry.  The parking garage is full."

    # Display an input that waits for an amount from the user and stores it in a variable
    def payForParking(self):
        payment = input("Please enter something to pay for your parking")
        if payment != "":
            print("Your ticket has been paid.  Please exit within 15 minutes")  #The print statement is nest within the if statement, so it should execute
            self.currentTicket["paid"] = True
        else:
            print("Your ticket has NOT been paid.")  #The print statement is nest within the if statement, so it should execute
    
    def leaveGarage(self):
        if self.currentTicket["paid"] == True:
            print("Thank you and have a nice day")
            #(1) increment ticket and (2) increase parking space
        for ticket_number in range(self.amountTickets):
            if self.tickets[ticket_number] == True:
                self.tickets[ticket_number] = False
                self.parkingSpaces[ticket_number] = False
                break

# Instantiate.

parkingGarage = ParkingGarage(10)
result = parkingGarage.takeTicket()
print(result)
result = parkingGarage.takeTicket()
print(result)
result = parkingGarage.takeTicket()
print(result)
result = parkingGarage.takeTicket()
print(result)
result = parkingGarage.takeTicket()
print(result)

parkingGarage.payForParking()
parkingGarage.leaveGarage()