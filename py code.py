import uuid
from datetime import datetime
users = {}
vehicles = {}
rides = {}
bookings = {}
payments = {}
def gen_id():
    return str(uuid.uuid4())[:8]
def create_user():
    name = input("Enter name: ")
    role = input("Enter role (driver/passenger): ").lower()
    if role not in ["driver", "passenger"]:
        print("❌ Invalid role.")
        return
    user_id = gen_id()
    users[user_id] = {"id": user_id, "name": name, "role": role, "rating": 0, "rating_count": 0}
    print(f"✅ User created with ID: {user_id}")
def add_vehicle():
    driver_id = input("Enter driver ID: ")
    if driver_id not in users or users[driver_id]["role"] != "driver":
        print("❌ Invalid driver ID.")
        return
    reg_no = input("Enter vehicle reg no: ")
    seats = int(input("Enter number of seats: "))
    v_id = gen_id()
    vehicles[v_id] = {"id": v_id, "owner": driver_id, "reg_no": reg_no, "seats": seats}
    print(f"✅ Vehicle added with ID: {v_id}")
def create_ride():
    driver_id = input("Enter driver ID: ")
    vehicle_id = input("Enter vehicle ID: ")
    if driver_id not in users or users[driver_id]["role"] != "driver":
        print("❌ Invalid driver.")
        return
    if vehicle_id not in vehicles:
        print("❌ Vehicle not found.")
        return
    src = input("Enter source: ")
    dst = input("Enter destination: ")
    dist = float(input("Enter distance (km): "))
    fare = 30 + dist * 6
    seats = int(input("Enter available seats: "))
    r_id = gen_id()
    rides[r_id] = {"id": r_id, "driver": driver_id, "vehicle": vehicle_id,
                   "source": src, "destination": dst, "distance": dist,
                   "fare": fare, "seats": seats, "time": datetime.now()}
    print(f"✅ Ride created with ID: {r_id}, Fare per seat: ₹{fare}")
def search_rides():
    src = input("Enter source: ")
    dst = input("Enter destination: ")
    print("🔎 Matching Rides:")
    for r in rides.values():
        if src.lower() in r["source"].lower() and dst.lower() in r["destination"].lower() and r["seats"] > 0:
            print(f'ID: {r["id"]} | From {r["source"]} to {r["destination"]} | Fare ₹{r["fare"]} | Seats {r["seats"]}')
def book_ride():
    passenger_id = input("Enter passenger ID: ")
    if passenger_id not in users or users[passenger_id]["role"] != "passenger":
        print("❌ Invalid passenger.")
        return
    ride_id = input("Enter ride ID: ")
    if ride_id not in rides or rides[ride_id]["seats"] <= 0:
        print("❌ Ride not available.")
        return
    b_id = gen_id()
    rides[ride_id]["seats"] -= 1
    bookings[b_id] = {"id": b_id, "ride": ride_id, "passenger": passenger_id,
                      "status": "confirmed"}
    print(f"✅ Booking confirmed with ID: {b_id}")
def make_payment():
    b_id = input("Enter booking ID: ")
    if b_id not in bookings:
        print("❌ Booking not found.")
        return
    ride_id = bookings[b_id]["ride"]
    fare = rides[ride_id]["fare"]
    p_id = gen_id()
    payments[p_id] = {"id": p_id, "booking": b_id, "amount": fare, "status": "success"}
    bookings[b_id]["status"] = "paid"
    print(f"✅ Payment successful! Payment ID: {p_id}, Amount: ₹{fare}")
def give_rating():
    u_id = input("Enter user ID to rate: ")
    if u_id not in users:
        print("❌ User not found.")
        return
    rating = int(input("Enter rating (1–5): "))
    if rating < 1 or rating > 5:
        print("❌ Invalid rating.")
        return
    users[u_id]["rating_count"] += 1
    total = users[u_id]["rating"] * (users[u_id]["rating_count"] - 1) + rating
    users[u_id]["rating"] = round(total / users[u_id]["rating_count"], 2)
    print(f"✅ Rating updated. New rating: {users[u_id]['rating']}")
def menu():
    while True:
        print("\n🚗 Carpooling & Ride-Sharing App")
        print("1. Create User")
        print("2. Add Vehicle")
        print("3. Create Ride")
        print("4. Search Rides")
        print("5. Book Ride")
        print("6. Make Payment")
        print("7. Give Rating")
        print("8. Exit")
        choice = input("Enter choice: ")
        if choice == "1": create_user()
        elif choice == "2": add_vehicle()
        elif choice == "3": create_ride()
        elif choice == "4": search_rides()
        elif choice == "5": book_ride()
        elif choice == "6": make_payment()
        elif choice == "7": give_rating()
        elif choice == "8": break
        else: print("❌ Invalid choice.")
if __name__ == "__main__":
    menu()