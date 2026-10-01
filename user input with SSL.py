class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
l1 = SLL()

while True:
    print("\n----- MENU -----")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            n = int(input("How many nodes do you want to insert? "))

            for i in range(n):
                num = int(input(f"Enter value for node {i + 1}: "))
                l1.insert(num)

            print("All nodes inserted successfully.")

        case 2:
            l1.display()

        case 3:
            print("Program terminated.")
            break

        case _:
            print("Invalid choice!")
