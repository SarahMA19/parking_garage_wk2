class ParkingGarage():
    """
    class ParkingGarage ....
    
    """
    def __init__(self):
        self.parkspaces = {
            1 :{
            'paid' : False,
            'open' : True,
            'left?' : False
            },
            2 :{
            'paid' : False,
            'open' : True,
            'left?' : False
            },
            3: {
            'paid' : False,
            'open' : True,
            'left?' : False
            },
            4: {
            'paid' : False,
            'open' : True,
            'left?' : False
            },
            5 : {
            'paid' : False,
            'open' : True,
            'left?' : False
            },
        }

       

    def takeTicket(self):
       self.parkspaces['open'][False]
       
       


        
        #self.parkspaces{1:[2]}-= 1
        #self.parkspaces -= 1
        #print(f"There are now {self.tickets} available tickets!") 
        #("This should decrease the amount of tickets available by 1 
        #- This should decrease the amount of parkingSpaces available by 1 ")
        #print(f"There are now {self.parkingSpaces} available parking spaces!") 

    def payForParking(self):
        self.parkspaces = input("Pay amount:")
        print("You're ticket has been paid, you have 15 minutes to leave.")  
        
    def checkPaid(self):
         self.parkspaces = ['paid'] [True]
                                   
    def LeaveGarage(self):
            
    
        
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
                 

            
        
        
Car = ParkingGarage()
Car.run()

