class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time

class Cargo:
    def __init__(self, cargo_id, origin, destination, weight):
        self.cargo_id = cargo_id
        self.origin = origin
        self.destination = destination
        self.weight = weight

class AirlineSystem:
    def __init__(self):
        self.flights = []
        self.cargoes = []

    def add_flight(self, flight_number, origin, destination, departure_time, arrival_time):
        flight = Flight(flight_number, origin, destination, departure_time, arrival_time)
        self.flights.append(flight)
        print(f"Flight {flight_number} added successfully.")

    def add_cargo(self, cargo_id, origin, destination, weight):
        cargo = Cargo(cargo_id, origin, destination, weight)
        self.cargoes.append(cargo)
        print(f"Cargo {cargo_id} added successfully.")

    def view_flights(self):
        print("Current Flights:")
        for flight in self.flights:
            print(f"Flight Number: {flight.flight_number}, Origin: {flight.origin}, Destination: {flight.destination}, Departure Time: {flight.departure_time}, Arrival Time: {flight.arrival_time}")

    def view_cargoes(self):
        print("Current Cargoes:")
        for cargo in self.cargoes:
            print(f"Cargo ID: {cargo.cargo_id}, Origin: {cargo.origin}, Destination: {cargo.destination}, Weight: {cargo.weight}")

# Example usage
airline_system = AirlineSystem()

while True:
    print("\nAirline Scheduling and Cargo Schedules System")
    print("1. Add Flight")
    print("2. Add Cargo")
    print("3. View Flights")
    print("4. View Cargoes")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        flight_number = input("Enter flight number: ")
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        departure_time = input("Enter departure time: ")
        arrival_time = input("Enter arrival time: ")
        airline_system.add_flight(flight_number, origin, destination, departure_time, arrival_time)
    elif choice == '2':
        cargo_id = input("Enter cargo ID: ")
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        weight = input("Enter weight: ")
        airline_system.add_cargo(cargo_id, origin, destination, weight)
    elif choice == '3':
        airline_system.view_flights()
    elif choice == '4':
        airline_system.view_cargoes()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")