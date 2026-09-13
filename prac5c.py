# Implement Queue using List (Functions)

q = []


def Enqueue():
    if len(q) == size:
        print("Queue is Full!!!!")
    else:
        element = input("Enter the element: ")
        q.append(element)
        print(element, "is added to the Queue!")


def dequeue():
    if not q:
        print("Queue is Empty!!!")
    else:
        e = q.pop(0)
        print("Element removed!!:", e)


def display():
    print(q)


size = int(input("Enter the size of Queue: "))

while True:
    print("Select the Operation: 1.Add 2.Delete 3.Display 4.Quit")

    choice = int(input())

    if choice == 1:
        Enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        break

    else:
        print("Invalid Option!!!")
