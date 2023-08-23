flight_information = {
    "AI161E90": ("BLR", "BOM", 5600),
    "BR161F91": ("BOM", "BBI", 6750),
    "AI161F99": ("BBI", "BLR", 8210),
    "VS171E20": ("JLR", "BBI", 5500),
    "AS171G30": ("HYD", "JLR", 4400),
    "AI131F49": ("HYD", "BOM", 3499)
}

city_mappings = {
    "BLR": "Bengaluru",
    "BOM": "Mumbai",
    "BBI": "Bhubaneswar",
    "HYD": "Hyderabad",
    "JLR": "Jabalpur"
}

def get_flight_info(flight_code=None, source=None, destination=None):
    if flight_code:
        if flight_code in flight_information:
            src, dest, price = flight_information[flight_code]
            print(f"Flight Code: {flight_code}")
            print(f"Source: {city_mappings[src]}")
            print(f"Destination: {city_mappings[dest]}")
            print(f"Price: {price}")
        else:
            print("Flight not found.")
    elif source:
        matching_flights = [(code, src, dest, price) for code, (src, dest, price) in flight_information.items() if src == source]
        if matching_flights:
            print("Flights from", city_mappings[source])
            for code, src, dest, price in matching_flights:
                print(f"Flight Code: {code}")
                print(f"Destination: {city_mappings[dest]}")
                print(f"Price: {price}")
        else:
            print("No flights found from", city_mappings[source])
    elif destination:
        matching_flights = [(code, src, dest, price) for code, (src, dest, price) in flight_information.items() if dest == destination]
        if matching_flights:
            print("Flights to", city_mappings[destination])
            for code, src, dest, price in matching_flights:
                print(f"Flight Code: {code}")
                print(f"Source: {city_mappings[src]}")
                print(f"Price: {price}")
        else:
            print("No flights found to", city_mappings[destination])
    else:
        print("Please provide valid input.")

user_input_type = int(input("Enter 1 for Flight Code, 2 for source city, or 3 for destination city: "))
if user_input_type == 1:
    flight_code = input("Enter Flight Code: ")
    get_flight_info(flight_code=flight_code)
elif user_input_type == 2:
    source = input("Enter source city: ")
    get_flight_info(source=source)
elif user_input_type == 3:
    destination = input("Enter destination city: ")
    get_flight_info(destination=destination)
else:
    print("Invalid input type.")
