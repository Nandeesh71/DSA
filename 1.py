class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coeff, exp):
        if coeff == 0:
            return
        new_node = Node(coeff, exp)
        if self.head is None or self.head.exp < exp:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.exp > exp:
                current = current.next
            if current.next and current.next.exp == exp:
                current.next.coeff += coeff
                if current.next.coeff == 0:
                    current.next = current.next.next
            elif current.exp == exp:
                current.coeff += coeff
                if current.coeff == 0:
                    self.head = current.next
            else:
                new_node.next = current.next
                current.next = new_node

    def add(self, other):
        result = Polynomial()
        p1, p2 = self.head, other.head
        while p1 or p2:
            if p1 and (not p2 or p1.exp > p2.exp):
                result.insert_term(p1.coeff, p1.exp)
                p1 = p1.next
            elif p2 and (not p1 or p2.exp > p1.exp):
                result.insert_term(p2.coeff, p2.exp)
                p2 = p2.next
            else:
                result.insert_term(p1.coeff + p2.coeff, p1.exp)
                p1, p2 = p1.next, p2.next
        return result

    def subtract(self, other):
        result = Polynomial()
        p1, p2 = self.head, other.head
        while p1 or p2:
            if p1 and (not p2 or p1.exp > p2.exp):
                result.insert_term(p1.coeff, p1.exp)
                p1 = p1.next
            elif p2 and (not p1 or p2.exp > p1.exp):
                result.insert_term(-p2.coeff, p2.exp)
                p2 = p2.next
            else:
                result.insert_term(p1.coeff - p2.coeff, p1.exp)
                p1, p2 = p1.next, p2.next
        return result

    def multiply(self, other):
        result = Polynomial()
        p1 = self.head
        while p1:
            temp = Polynomial()
            p2 = other.head
            while p2:
                temp.insert_term(p1.coeff * p2.coeff, p1.exp + p2.exp)
                p2 = p2.next
            result = result.add(temp)
            p1 = p1.next
        return result

    def display(self):
        terms = []
        current = self.head
        while current:
            if current.coeff > 0 and current != self.head:
                terms.append(f"+ {current.coeff}x^{current.exp}")
            elif current.coeff < 0:
                terms.append(f"- {-current.coeff}x^{current.exp}")
            else:
                terms.append(f"{current.coeff}x^{current.exp}")
            current = current.next
        return " ".join(terms) if terms else "0"


# Example Usage
if __name__ == "__main__":
    # First polynomial: 3x^3 + 2x^2 + x
    poly1 = Polynomial()
    poly1.insert_term(3, 3)
    poly1.insert_term(2, 2)
    poly1.insert_term(1, 1)

    # Second polynomial: 4x^2 + 2x + 1
    poly2 = Polynomial()
    poly2.insert_term(4, 2)
    poly2.insert_term(2, 1)
    poly2.insert_term(1, 0)

    print("Polynomial 1:", poly1.display())
    print("Polynomial 2:", poly2.display())
    print("Addition:", poly1.add(poly2).display())
    print("Subtraction:", poly1.subtract(poly2).display())
    print("Multiplication:", poly1.multiply(poly2).display())
