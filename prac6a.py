# Add two polynomials using linked list

class Node:
    def __init__(self, data, power):
        self.data = data
        self.power = power
        self.next = None

    # Update node value
    def updateRecord(self, data, power):
        self.data = data
        self.power = power


class AddPolynomial:
    def __init__(self):
        self.head = None

    # Display given polynomial nodes
    def display(self):
        if self.head == None:
            print("Empty Polynomial")
            return

        print(" ", end="")

        temp = self.head

        while temp != None:
            if temp != self.head:
                print("+", temp.data, end="")
            else:
                print(temp.data, end="")

            if temp.power != 0:
                print("x^", temp.power, end=" ", sep="")

            temp = temp.next

        print()


    # Add node with given data and power
    def addNode(self, data, power):
        if self.head == None:
            self.head = Node(data, power)
        else:
            node = None
            temp = self.head
            location = None

            # Find the valid new node location
            while temp != None and temp.power >= power:
                location = temp
                temp = temp.next

            if location != None and location.power == power:
                location.data = location.data + data
            else:
                node = Node(data, power)

                if location == None:
                    # Add node in beginning
                    node.next = self.head
                    self.head = node
                else:
                    # Add node in intermediate or end
                    node.next = location.next
                    location.next = node


    # Add two polynomial
    def addTwoPolynomials(self, other):
        result = None
        tail = None
        node = None

        first = self.head
        second = other.head

        # Add two polynomials
        while first != None or second != None:

            node = Node(0, 0)

            if result == None:
                result = node

            if first != None and second != None:

                if first.power == second.power:
                    node.updateRecord(
                        first.data + second.data,
                        first.power
                    )

                    first = first.next
                    second = second.next

                elif first.power > second.power:
                    node.updateRecord(
                        first.data,
                        first.power
                    )

                    first = first.next

                else:
                    node.updateRecord(
                        second.data,
                        second.power
                    )

                    second = second.next

            elif first != None:
                node.updateRecord(first.data, first.power)
                first = first.next

            else:
                node.updateRecord(second.data, second.power)
                second = second.next

            if tail == None:
                tail = node
            else:
                tail.next = node
                tail = node

        return result


def main():
    poly1 = AddPolynomial()
    poly2 = AddPolynomial()
    result = AddPolynomial()

    # Add nodes in polynomial poly1
    poly1.addNode(9, 3)
    poly1.addNode(4, 2)
    poly1.addNode(3, 0)
    poly1.addNode(7, 1)
    poly1.addNode(3, 4)

    # Add nodes in polynomial poly2
    poly2.addNode(7, 3)
    poly2.addNode(4, 0)
    poly2.addNode(6, 1)
    poly2.addNode(1, 2)

    # Display Polynomial nodes
    print("\nPolynomial A")
    poly1.display()

    print("Polynomial B")
    poly2.display()

    result.head = poly1.addTwoPolynomials(poly2)

    # Display calculated result
    print("Result")
    result.display()


if __name__ == "__main__":
    main()
