
class ParkingGarage():
    """
    What represents a parking garage
    
    """
    def __init__(self, ticket, spaces, pay, currentTicket, leave):
    
       self.ticket = 5
       self.spaces = 5
       self.pay = pay
       self.currentTicket = currentTicket
       self.leave = leave
       

    def takeTicket(self):
         self.ticket -= 1
         self.spaces -= 1
         print(f'Great, here is your ticket. There are now {self.ticket} tickets & {self.spaces} spaces left') 

    def addPayment(self):
        responce = input("Type amount you are going to pay: $")
        self.pay.append(responce)
              
    def showPaid(self):
        print("Here is your reciept for what you have paid:$")
        for i in self.pay:
            print(i)
                                   
    def LeaveGarage(self):
        if self.currentTicket == i:
            print("Thank you, have a nice day!")
        elif input("You must pay for your parking before you leave, please pay now: $ "):
            print("Thank you, have a nice day!")
      
        
    def run(self): 
        while True:
            responce = input('Welcome to "Saronia Parking"! Type t for ticket, p for pay or l to leave.')
            
            if responce.lower() == "t":
                self.takeTicket()
            
            if responce.lower() == "p":
                 self.addPayment()
                 self.showPaid()

            if responce.lower() == "l":
                 self.LeaveGarage()
                 break
                 

    
Car = ParkingGarage(0,0,[],0, 0)
Car.run()


# def __init__(self):
#         self.parkspaces = {
#             1 :{
#             'paid' : False,
#             'open' : True,
#             'left?' : False
#             },
#             2 :{
#             'paid' : False,
#             'open' : True,
#             'left?' : False
#             },
#             3: {
#             'paid' : False,
#             'open' : True,
#             'left?' : False
#             },
#             4: {
#             'paid' : False,
#             'open' : True,
#             'left?' : False
#             },
#             5 : {
#             'paid' : False,
#             'open' : True,
#             'left?' : False
#             },
#         }
