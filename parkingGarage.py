class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.total_tickets = total_tickets
        self.total_parking_spaces = total_parking_spaces
        self.current_ticket = {}
        self.tickets = [i for i in range(1, total_tickets + 1)]
        self.parking_spaces = [i for i in range(1, total_parking_spaces + 1)]

def take_ticket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parking_spaces.pop(0)
            self.current_ticket = {"ticket_number": ticket_number, "paid": False, "parking_space": parking_space}
            print(f"Ticket {ticket_number} issued. Parking space {parking_space} is available.")
        else:
            print("Sorry,Garage is Full.")

    def payParking(self):

        payment = input("Please enter the amount for parking: $")
        if payment:
            print("Payment received. You have 15 minutes to leave the garage.")

    def leaving(self):
        payment = input("Please make a payment before leaving. Enter the payment amount: $")
        if payment:
                self.currentTicket['paid'] = True
                print("Payment received. Thank you for visiting! Have a nice day.")
                

customer = ParkingGarage()

while True:
    print("\nOptions:")
    print("1. Take a ticket")
    print("2. Pay for parking")
    print("3. Leave the garage")
    print("4. Exit")
    choice = input("Select an option (1/2/3/4): ")

    if choice == '1':
            customer.takeTicket()
    elif choice == '2':
            customer.payParking()
    elif choice == '3':
            customer.leaving()
    elif choice == '4':
        break
    else:
        print("Invalid option. Please choose a valid option.")
