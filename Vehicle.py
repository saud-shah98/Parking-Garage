class Vehicle:
    def __init__(self, license_number, vehicle_type):
        self.license_number = license_number
        self.vehicle_type = vehicle_type
        self.ticket = None
    
    def assign_ticket(self, ticket):
        self.ticket = ticket
        print(f"Ticket assigned to vehicle {self.license_number}: {ticket}")

    def __str__(self):
        return f"Vehicle(license_number={self.license_number}, type={self.vehicle_type}, ticket={self.ticket})"
