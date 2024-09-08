class ParkingFloor:
    def __init__(self, name):
        self.name = name
        self.parking_slots = []

    def add_parking_slot(self, spot):
        self.parking_slots.append(spot)

    def get_available_spots(self):
        return [slot for slot in self.parking_slots if slot.get_is_free()]

    def get_spot_details(self):
        details = []
        for spot in self.parking_slots:
            if spot.get_is_free():
                details.append(f"Spot {spot.number}: Available")
            else:
                vehicle_info = f"Car {spot.vehicle.license_number}" if spot.vehicle else "Occupied by unknown vehicle"
                details.append(f"Spot {spot.number}: {vehicle_info}")
        return details
