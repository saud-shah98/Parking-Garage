class ParkingSpot:
    def __init__(self, number, spot_type):
        self.number = number
        self.spot_type = spot_type
        self.free = True
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        if self.free:
            self.vehicle = vehicle
            self.free = False
        else:
            raise Exception("Spot already occupied")

    def remove_vehicle(self):
        if not self.free:
            self.vehicle = None
            self.free = True
        else:
            raise Exception("Spot is already free")

    def get_is_free(self):
        return self.free

    def __str__(self):
        return f"Spot {self.number} ({self.spot_type}): {'Occupied' if not self.free else 'Free'}"
