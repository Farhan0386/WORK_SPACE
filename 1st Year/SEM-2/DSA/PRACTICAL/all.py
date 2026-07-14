# ================================
# 🔥 DSA PRACTICAL ALL-IN-ONE FILE
# ================================

# --------------------------------
# 1. LINEAR SEARCH
# --------------------------------
def linear_search(arr, key):
    # har element ko check karte hain
    for i in range(len(arr)):
        if arr[i] == key:   # match mila
            return i        # index return
    return -1               # nahi mila


# --------------------------------
# 2. BINARY SEARCH (sorted array)
# --------------------------------
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2   # middle index nikalte hain

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1   # right side search
        else:
            high = mid - 1  # left side search

    return -1


# --------------------------------
# 3. INSERTION SORT
# --------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):   # 2nd element se start
        key = arr[i]               # current element store
        j = i - 1

        # left side me bada element ho to shift
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]      # shift right
            j -= 1

        arr[j+1] = key             # correct position pe insert

    return arr


# --------------------------------
# 4. BUBBLE SORT
# --------------------------------
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):  # last elements sorted ho jate hain
            if arr[j] > arr[j+1]:
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# --------------------------------
# 5. RECURSION (FACTORIAL)
# --------------------------------
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n-1)  # recursive call


# --------------------------------
# 6. RECURSION (FIBONACCI)
# --------------------------------
def fibonacci(n):
    if n <= 1:   # base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# --------------------------------
# 7. STACK (LIFO)
# --------------------------------
class Stack:
    def __init__(self):
        self.items = []   # list as stack

    def push(self, x):
        self.items.append(x)   # last me add

    def pop(self):
        if len(self.items) == 0:
            return "Underflow"
        return self.items.pop()   # last remove

    def peek(self):
        if len(self.items) == 0:
            return "Empty"
        return self.items[-1]   # top element


# --------------------------------
# 8. QUEUE (FIFO)
# --------------------------------
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)   # rear se add

    def dequeue(self):
        if len(self.items) == 0:
            return "Empty"
        return self.items.pop(0)   # front se remove


# --------------------------------
# 9. LINKED LIST
# --------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # next pointer


class LinkedList:
    def __init__(self):
        self.head = None   # starting point

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head   # old head connect
        self.head = new        # head update

    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next   # last tak jao

        temp.next = new   # attach at end

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next   # bypass node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# --------------------------------
# 10. 2D ARRAY (Transpose)
# --------------------------------
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])   # swap row/col
        result.append(new_row)

    return result


# --------------------------------
# 🔥 TEST SECTION (optional)
# --------------------------------
if __name__ == "__main__":
    print("Linear Search:", linear_search([1,2,3,4], 3))
    print("Binary Search:", binary_search([1,2,3,4,5], 4))

    print("Insertion Sort:", insertion_sort([4,2,1,3]))
    print("Bubble Sort:", bubble_sort([5,3,2,1]))

    print("Factorial:", factorial(5))
    print("Fibonacci:", fibonacci(6))

    s = Stack()
    s.push(10)
    s.push(20)
    print("Stack pop:", s.pop())

    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    print("Queue dequeue:", q.dequeue())

    l = LinkedList()
    l.insert_begin(10)
    l.insert_end(20)
    l.display()

    print("Transpose:", transpose([[1,2],[3,4]]))