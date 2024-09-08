from datetime import datetime
class ParkingTicket:
    def __init__(self, ticket_number, issued_at, payed_amount=0, status="Issued"):
        self.ticket_number = ticket_number
        self.issued_at = issued_at
        self.payed_at = None
        self.payed_amount = payed_amount
        self.status = status

    def mark_as_paid(self, amount):
        self.payed_amount = amount
        self.payed_at = datetime.now()
        self.status = "Paid"

    def __str__(self):
        return (f"Ticket Number: {self.ticket_number}\n"
                f"Issued At: {self.issued_at}\n"
                f"Payed At: {self.payed_at if self.payed_at else 'Not Paid'}\n"
                f"Payed Amount: {self.payed_amount}\n"
                f"Status: {self.status}")
