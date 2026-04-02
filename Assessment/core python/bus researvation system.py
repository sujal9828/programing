routes = {
    1: ["mumbai to pune", 500],
    2: ["gujrat to rajasthan", 600],
    3: ["delhi to punjab", 700],
    4: ["kolkata to assam", 800],
}

tickets = {}
ticket_counter = 1001


def show_routes():
    print("\n Available routes :")
    for key in routes:
        print(key, "-", routes[key][0], " - Rs.", routes[key][1])


def book_ticket():
    global ticket_counter

    name = input("enter your name :")
    age = int(input("enter your age :"))
    mobile = input("enter your mobile number :")

    show_routes()
    route_choice = int(input("enter the route number you want to book :"))

    if route_choice in routes:
        print("invalid route !!")
        return

        route_name = routes[route_choice][0]
        price = routes[route_choice][1]

        seat_count = 0

        for t in tickets:
            if tickets[t]["route"] == route_name:
                seat_count += 1

        if seat_count >= 40:
            print("sorry, buss full")
            return

        seat_number = seat_count + 1
        ticket_id = "T" +str(ticket_counter)
        ticket_counter += 1

        tickets[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route_name,
            "price": price,
            "seat_number": seat_number
        }

        print("ticket booked successfully !!")
        print("ticket id :", ticket_id)
        print("seat :", seat_number)

def view_tickets():
    tid = input("enter ticket id :")

    if tid not in tickets:
        print("invalid ticket id !!")
        return

    t = tickets[tid]

    print("\n ticket details :")
    print("name :", t["name"])
    print("age :", t["age"])
    print("mobile :", t["mobile"])
    print("route :", t["route"])
    print("price :", t["price"])
    print("seat number :", t["seat_number"])

def cancel_ticket():
    tid = input("enter ticket id :")

    if tid not in tickets:
        print(" ticket not found !!")
        return

    del tickets[tid]
    print("ticket cancelled successfully !!")

# main loop #

while True:
    print("\n bus reservation system")
    print("1. show routes")
    print("2. book ticket")
    print("3. view ticket")
    print("4. cancel ticket")
    print("5. exit")

    choice = int(input("enter your choice :"))

    if choice == 1:
        show_routes()
        
    elif choice == 2:
        book_ticket()

    elif choice == 3:
        view_tickets()

    elif choice == 4:
        cancel_ticket()

    elif choice == 5:
        print("thank you for using the bus reservation system !!")
        break

    else:
        print("invalid choice !!")
