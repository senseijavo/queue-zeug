# Realisiert eine Schlange als Klasse mit Zeigern
# Quelle https://www.delftstack.com/de/howto/python/queue-implementation-in-python/
#        warteschlangenimplementierung-mit-verkn%C3%BCpften-listen-in-python

# Die Knotenklasse für ein Element
class Node:
    def __init__(self, data):
        self.data = data        
        self.next = None

# Die Trivialschlange mit den Methoden
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front is None:
            return True
        return False

    def enQueue(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def deQueue(self):
        if self.isEmpty():
            print("Queue ist leer.")
        else:
            # Beachte die Reihenfolge der Operationen
            element = self.front
            nextFront = self.front.next
            self.front = nextFront
            value = element.data
            del element
            return value

    def length(self):
        count = 0
        if self.front is None:
            return count
        else:
            temp = self.front
            while temp is not None:
                count += 1
                temp = temp.next
            return count


# Test
if __name__ == '__main__':
    myQueue = Queue()
    print("enqueuing 10")
    myQueue.enQueue(10)
    print("Länge:", myQueue.length())
    print("enqueuing 15")
    myQueue.enQueue(15)
    print("Länge:", myQueue.length())
    print("enqueuing 20")
    myQueue.enQueue(20)
    print("Länge:", myQueue.length())
    x = myQueue.deQueue()
    print("dequeued: ", x)
    print("Länge:", myQueue.length())
    y = myQueue.deQueue()
    print("dequeued: ", y)
    z = myQueue.deQueue()
