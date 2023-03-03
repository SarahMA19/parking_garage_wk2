class ParkingGarage():
    """
    class ParkingGarage ....
    
    """
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
       

    def takeTicket(self):
        self.tickets -= 1
        self.parkingSpaces -= 1
        print(f"There are now {self.tickets} available tickets!") 
        #("This should decrease the amount of tickets available by 1 
        #- This should decrease the amount of parkingSpaces available by 1 ")
        print(f"There are now {self.parkingSpaces} available parking spaces!") 

    def payForParking(self,):
        self.currentTicket = input("Pay amount:")
        print("You're ticket has been paid, you have 15 minutes to leave.")  
        
    def checkPaid(self, paid):
         self.currentTicket = paid
        
    def LeaveGarage(self):
            if self.checkPaid == True:
                 print('Thank you, have a nice day!')
            elif self.checkPaid != True:
                 input('Please pay your parking ticket.')
    

    



        
    def run(self): 
        while True:
            responce = input('Welcome to the parking garage, there are 5 available spots. Type t for ticket, p for pay or l to leave.')
            
            if responce.lower() == "t":
                self.takeTicket()
            
            if responce.lower() == "p":
                 self.payForParking()

            if responce.lower() == "l":
                 self.checkPaid(self)
                 self.LeaveGarage()
                 
                 break
                 

            
        
        
Car = ParkingGarage(5, 5, 5,)
Car.run()