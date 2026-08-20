class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price
        self.category = "Standard"

    def display_info(self):
        print(f"No: {self.vehicle_number} | Brand: {self.brand} | Category: {self.category} | Price: ${self.price:,.2f}")


class LuxuryVehicle(Vehicle):
    def __init__(self, vehicle_number, brand, price):
        super().__init__(vehicle_number, brand, price)
        self.category = "Luxury"


class EconomyVehicle(Vehicle):
    def __init__(self, vehicle_number, brand, price):
        super().__init__(vehicle_number, brand, price)
        self.category = "Economy"


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the showroom.")
            return
        print("\n--- Showroom Vehicle Inventory ---")
        for vehicle in self.vehicles:
            vehicle.display_info()

    def generate_valuation_table(self):
        if not self.vehicles:
            return []

        n = len(self.vehicles)
        dp = [0.0] * n
        dp[0] = self.vehicles[0].price

        for i in range(1, n):
            dp[i] = dp[i - 1] + self.vehicles[i].price

        return dp


if __name__ == "__main__":
    showroom = Showroom()
    showroom.add_vehicle(EconomyVehicle("KA-01-H-1234", "Toyota Corolla", 22000))
    showroom.add_vehicle(LuxuryVehicle("KA-05-Z-9999", "BMW 7 Series", 95000))
    showroom.add_vehicle(EconomyVehicle("KA-03-A-5678", "Hyundai i20", 15000))

    showroom.display_all_vehicles()
    cumulative_table = showroom.generate_valuation_table()
    
    print("\n--- Tabulated Cumulative Inventory Value ---")
    for idx, vehicle in enumerate(showroom.vehicles):
        print(f"Up to {vehicle.brand} ({vehicle.vehicle_number}): Cumulative Value = ${cumulative_table[idx]:,.2f}")