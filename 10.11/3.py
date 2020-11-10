class Ticket():
    def __init__(self, price, name):
        self.name = name
        self.price = price

class Conductor():
    def __init__(self):
        self.money = 0
        self.tickets = []
    #Create a brand new type of tickets to sell
    def addTicketType(self, ticketName, ticketPrice):
        ticket = Ticket(ticketPrice, ticketName)
        self.tickets.append(ticket)
    #Sell ticket to the traveler by name of ticket
    def sellTicket(self, traveler, ticketName):
        currentTicket = None
        for ticket in self.tickets:
            if(ticket.name == ticketName):
                currentTicket = ticket
        if(currentTicket is None):
            print('Conductor does not have this type of tickets')
        elif(traveler.money >= currentTicket.price):
            traveler.money -= currentTicket.price
            traveler.ticket += 1
            self.money += currentTicket.price
        else:
            print('Traveler does not have enough money')

    
class Traveler():
    def __init__(self, amountOfMoney):
        self.money = amountOfMoney
        self.ticket = 0
    def buyTicket(self, conductor, name):
        if(self.ticket == 1):
            print("Traveler already has the ticket")
        else:
            conductor.sellTicket(self, name)



conductor = Conductor()
conductor.addTicketType('ToAstana', 200)
conductor.addTicketType('ToNurSultan', 324)
traveler = Traveler(550000)
traveler.buyTicket(conductor, 'ToNurSultan')
traveler.buyTicket(conductor, 'ToAstana')
print(traveler.ticket)