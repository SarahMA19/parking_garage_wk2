
class ParkingGarage():
    """
    What represents a parking garage
    
    """
    def __init__(self, spaces, pay, leave):
       self.spaces = 5
       self.pay = pay
       self.leave = leave
       
       
    def takeTicket(self):
         if self.spaces == 0:
            print("There are not more parking spaces available")
         else:   
            self.spaces -= 1
            print(f'Great, here is your ticket. There are now {self.spaces} spaces left')

    def addPayment(self):
        if self.spaces < 5:
            input("Give me some money")
            self.pay = True
            print ("Thanks, have a great day!")
        else:
            print ("What are you a ghost? **You cannot pay before you have recieved a ticket**")
                                   
    def LeaveGarage(self):
        if self.spaces >= 5:
            print("You crazy **You cannot leave, if you have not recieved a ticket**")
        elif self.pay == True:
            print("Thank you, have a nice day!")
        else:
            input("You must pay for your parking before you leave!")
            print("Thanks for paying")
        self.pay == False
        
    def run(self): 
        while True:
            response = input('Welcome to "Saronia Parking"! Type t for ticket, p for pay or l to leave.')
            
            if response.lower() == "t":
                self.takeTicket()
            
            if response.lower() == "p":
                 self.addPayment()

            if response.lower() == "l":
                 self.LeaveGarage()
                 
                 

    
Car = ParkingGarage(0,0,0,)
Car.run()


