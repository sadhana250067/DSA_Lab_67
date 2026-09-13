class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head

        print("Queue is:[", end="")

        while temp:
            print(temp.data, end=", ")
            temp = temp.next

        print("]")

    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = Node(data)

        self.display()

    def dequeue(self):
        if self.head is None:
            print("Queue is Empty")
            self.display()
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            self.display()
            return data


def main():
    Q = Queue()

    print("1.enqueue\n2.dequeue\n3.exit")

    while 1:
        choice = input("Enter your option: ")

        if choice == "1":
            d = int(input("Enter data: "))
            Q.enqueue(d)

        elif choice == "2":
            print("Deleted element is:", Q.dequeue())

        else:
            break


if __name__ == "__main__":
    main()
