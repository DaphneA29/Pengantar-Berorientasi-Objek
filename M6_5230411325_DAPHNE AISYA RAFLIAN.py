class Order:
    def __init__(self, ID, name, details):
        self.__ID = ID  
        self.name = name
        self.details = details

    def set_order(self):
        print("Setting order...")

    def get_ID(self):
        return self.__ID


class Delivery:
    def __init__(self, id, name, information, date, address):
        self.__id = id 
        self.name = name
        self.information = information
        self.date = date
        self.address = address

    def process_delivery(self):
        print("Processing delivery...")

    def get_id(self):
        return self.__id


def main_menu():
    orders = []
    deliveries = []

    while True:
        print("\n----- Main Menu -----")
        print("1. Create Order      |")
        print("2. View Orders       |")
        print("3. Create Delivery   |")
        print("4. View Deliveries   |")
        print("5. Process Delivery  |")
        print("6. Exit              |")
        choice = input("Choose an option !: ")

        if choice == '1':
            ID = input("Enter Order ID: ")
            name = input("Enter Order Name: ")
            details = input("Enter Order Details: ")
            order = Order(ID, name, details)
            order.set_order()
            orders.append(order)
            print("Order created successfully. =^.^= !")

        elif choice == '2':
            if not orders:
                print("No orders available.")
            else:
                for i, order in enumerate(orders, start=1):
                    print(f"\nOrder {i}:")
                    print(f"ID: {order.get_ID()}")
                    print(f"Name: {order.name}")
                    print(f"Details: {order.details}")

        elif choice == '3':
            id = input("Enter Delivery ID: ")
            name = input("Enter Delivery Name: ")
            information = input("Enter Delivery Information: ")
            date = input("Enter Delivery Date: ")
            address = input("Enter Delivery Address: ")
            delivery = Delivery(id, name, information, date, address)
            deliveries.append(delivery)
            print("Delivery created successfully. =^.^= !")

        elif choice == '4':
            if not deliveries:
                print("No deliveries available. T_T")
            else:
                for i, delivery in enumerate(deliveries, start=1):
                    print(f"\nDelivery {i}:")
                    print(f"ID: {delivery.get_id()}")
                    print(f"Name: {delivery.name}")
                    print(f"Information: {delivery.information}")
                    print(f"Date: {delivery.date}")
                    print(f"Address: {delivery.address}")

        elif choice == '5':
            if not deliveries:
                print("No deliveries to process. T_T")
            else:
                for i, delivery in enumerate(deliveries, start=1):
                    print(f"Processing Delivery {i}: {delivery.name}")
                    delivery.process_delivery()
                    print(f"Delivery {i} processed.")

        elif choice == '6':
            print("Exiting... BYE!! ^_^")
            break

        else:
            print("Invalid choice, please try again. T_T")


if __name__ == "__main__":
    main_menu()
