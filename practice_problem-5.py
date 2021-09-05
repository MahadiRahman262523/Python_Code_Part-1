# write a class train which has methods to book a ticket ,
# get status(no of seats) and get fare info of trains running 
# under Indian Railways

class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def getStatus(self):
        print("************************************************")
        print(f"The name of the train {self.name}")  
        print(f"The available seats of the train {self.seats}")
        print("*************************************************")
        
    def fareInfo(self):
        print(f"The price of the ticket is {self.fare} Taka")
        
    def bookTicket(self):
        if(self.seats > 0):
            print(f"Your Ticket has been booked!! Your seat number is {self.seats}")
            self.seats = self.seats-1 
        else:
            print("The Train is full")   
        
        
intercity = Train("Intercity Express:14015",90,300)

intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()

intercity.fareInfo()               




