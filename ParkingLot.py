import random
from datetime import datetime
from ParkingTicket import ParkingTicket
from ParkingFloor import ParkingFloor
from ParkingSpot import ParkingSpot

class ParkingLot:
    def __init__(self, address):
        self.address = address
        self.floors = []
        self.issued_tickets = set()

        # Initialize default floors and parking spots
        self.initialize_default_floors()

    def initialize_default_floors(self):
        # Initialize Floors
        basement = ParkingFloor("Basement")
        ground = ParkingFloor("Ground Floor")
        s1 = ParkingFloor("First Floor")

        # Add Parking Spots to Floors
        for i in range(5):
            basement.add_parking_slot(ParkingSpot(i + 1, "Regular"))
            ground.add_parking_slot(ParkingSpot(i + 6, "Regular"))
            s1.add_parking_slot(ParkingSpot(i + 11, "Regular"))

        # Add Floors to Parking Lot
        self.floors.append(basement)
        self.floors.append(ground)
        self.floors.append(s1)

    def add_new_floor(self, name):
        new_floor = ParkingFloor(name)
        
        # Populate the new floor with default parking spots
        for i in range(5):  # Adjust the range for the number of spots
            new_floor.add_parking_slot(ParkingSpot(i + 1, "Regular"))
        
        self.floors.append(new_floor)
        return new_floor.name

    def display_status(self):
        status_message = []
        for floor in self.floors:
            floor_status = [f"Floor: {floor.name}"]
            floor_status.extend(floor.get_spot_details())
            status_message.append("\n".join(floor_status))
        return "\n\n".join(status_message)

    def get_new_parking_ticket(self, vehicle):
        if vehicle.license_number in self.issued_tickets:
            return None
        
        for floor in self.floors:
            available_spots = floor.get_available_spots()
            if available_spots:
                spot = available_spots[0]
                ticket_number = random.randint(1000, 9999)
                issued_at = datetime.now()
                ticket = ParkingTicket(ticket_number, issued_at)
                spot.assign_vehicle(vehicle)
                vehicle.assign_ticket(ticket)
                self.issued_tickets.add(vehicle.license_number)
                return {"vehicle": vehicle, "floor": floor, "spot": spot, "ticket": ticket}
        return None
