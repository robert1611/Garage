#Class: ParkingGarage

class ParkingGarage:
    def __init__(self, amountTickets):
        self.tickets = [False] * amountTickets   #boolean value
        self.parkingSpaces = [False] * amountTickets #boolean value
        self.currentTicket = {}   #dictoinary for a current log for who pays, enters, leaves
        for i in range(amountTickets):
            self.currentTicket[i] = False

    def takeTicket(self):
        if self.tickets.count == 11:
            return 
            self.tickets[free_spot] = True
            self.parkingSpace[free_spot] = True
            print(f"You get ticket {free_spot}. Plaese provide payment")
            self.payForParking(free_spot)
        else:
            print("Thers is no parking spaces left. Please wait for new spot") #if there's one avialable


    def payForParking(self):


    def leaveGarage(self):