class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.nextE
        return " -> ".join(elements)

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current
            current = current.nextE
        return None

    def delete(self, e):
        if self.head is None:
            return
        if self.head.data == e:
            self.head = self.head.nextE
            self.size -= 1
            return
        current = self.head
        while current.nextE:
            if current.nextE.data == e:
                current.nextE = current.nextE.nextE
                self.size -= 1
                return
            current = current.nextE

    def append(self, e, func=None):
        new_element = Element(e)
        if self.head is None:
            self.head = new_element
            self.tail = new_element
            self.size += 1
            return
        if func is None:
            func = lambda x, y: x >= y
        if func(e, self.head.data):
            new_element.nextE = self.head
            self.head = new_element
            self.size += 1
            return
        current = self.head
        while current.nextE:
            if func(e, current.nextE.data):
                new_element.nextE = current.nextE
                current.nextE = new_element
                self.size += 1
                return
            current = current.nextE
        current.nextE = new_element
        self.tail = new_element
        self.size += 1
