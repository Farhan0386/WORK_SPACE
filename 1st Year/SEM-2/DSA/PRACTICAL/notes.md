# 📘 DSA VIVA NOTES (DETAILED HINGLISH) - EXPANDED VERSION

---

# 🟢 ALGORITHM

**Definition:**
Algorithm ek finite step-by-step procedure hota hai jo kisi problem ko solve karta hai aur har step clearly defined hota hai.

**Important Points:**

* Finite hona chahiye (end hona chahiye)
* Input leta hai
* Output deta hai
* Deterministic hona chahiye (same input = same output)
* Language independent hota hai
* Unambiguous instructions honi chahiye

**Characteristics of Good Algorithm:**
* **Correctness:** Sahi answer dena chahiye har case me
* **Efficiency:** Time aur space optimize hona chahiye
* **Scalability:** Bade data par bhi work karna chahiye
* **Simplicity:** Samajhna aur implement karna aasan hona chahiye
* **Feasibility:** Practical roop se possible hona chahiye

**Example Algorithm (Linear Search):**
```
Procedure: LinearSearch(array A, value target)
1. i = 0
2. while i < length(A):
   a. if A[i] == target:
      return i
   b. i = i + 1
3. return -1  (not found)
```

**Real World Examples:**
* Recipe cooking banane ke liye
* GPS navigation
* Recipe khana banane ke liye

**Viva Line:**
"Algorithm ek systematic way hai problem solve karne ka jisme steps clearly defined ho, deterministic ho, aur finite time me end ho."

---

# 🟢 ASYMPTOTIC NOTATION

**Definition:**
Ye batata hai algorithm kitna efficient hai (time ya space ke hisaab se). Algorithm ke performance ko large inputs (n → ∞) par analyze karte hain.

**Kyu Zaroori Hai:**
* Exact time measure nahi kar sakte (system, compiler, processor par depend karta hai)
* Growth rate samajhna zaroori hai
* Algorithms ko compare karna aasan hota hai

**Growth Rate Concept:**
* n = 10: Zyada difference nahi
* n = 1000: Bada difference
* n = 10000: Very big difference

---

## Big O (O) - Worst Case Analysis

* **Maximum time** algorithm ko lag sakta hai
* Kisi bhi condition me ye worst hota hai
* Safe upper bound provide karta hai
* Zyada commonly use hota hai

👉 Example: Linear search → O(n)
- Agar element last position par ho
- Ya element array me exist nahi karta

**Common Big O Complexities:**
* **O(1)** - Constant time (array index access, hash lookup)
* **O(log n)** - Logarithmic (binary search)
* **O(n)** - Linear (linear search, loop through array)
* **O(n log n)** - Linearithmic (merge sort, quick sort average)
* **O(n²)** - Quadratic (bubble sort, nested loops)
* **O(n³)** - Cubic (triple nested loops)
* **O(2^n)** - Exponential (recursive fibonacci)
* **O(n!)** - Factorial (permutations, combinations)

**Complexity Ranking (Fastest to Slowest):**
```
O(1) << O(log n) << O(n) << O(n log n) << O(n²) << O(n³) << O(2^n) << O(n!)
```

**Practical Examples:**
| Operation | Big O | Example |
|-----------|-------|---------|
| Array indexing | O(1) | arr[5] |
| Binary search | O(log n) | sorted array search |
| Linear search | O(n) | unsorted array search |
| Merge sort | O(n log n) | efficient sorting |
| Bubble sort | O(n²) | inefficient sorting |
| Fibonacci recursive | O(2^n) | exponential growth |

---

## Omega (Ω) - Best Case Analysis

* **Minimum time** algorithm ko lag sakta hai
* Ideal condition/lucky scenario me ye minimum time hota hai
* Lower bound provide karta hai
* Kam commonly use hota hai

👉 Example: Linear search → Ω(1)
- Agar element first position par ho immediately mil jaaye

---

## Theta (Θ) - Average Case Analysis

* **Average time** algorithm ko lag sakta hai
* Real world scenario, typical case
* Zyada practical aur useful hota hai

👉 Example: Linear search → Θ(n/2) = Θ(n)
- Roughly average n/2 comparisons, but growth is still O(n)

---

**Quick Comparison Table:**
| Case | Notation | Scenario | Example |
|------|----------|----------|---------|
| Worst | Big O | Maximum guarantee | array ko search, element last me |
| Best | Omega (Ω) | Minimum guarantee | array search, element first me |
| Average | Theta (Θ) | Typical scenario | array search, random position |

**Space Complexity Bhi Zaroori Hai:**
* O(1) - Constant space (no extra space)
* O(n) - Linear space (array store)
* O(n²) - Quadratic space (2D array)
* O(log n) - Space used by recursion call stack

---

**Viva Line:**
"Big O worst case batata hai jaha maximum guarantee hota hai. Omega best case hai aur Theta average case hai. Real world me Big O zyada important hai kyunki worst case scenario ke liye prepare rehna chahiye."

---

# 🟢 RECURSION

**Definition:**
Recursion me function khud ko call karta hai (self-reference) jab tak base condition satisfy na ho. Divide and conquer approach follow karta hai.

**Important Components:**

* **Base Case:** Recursion kab rukni hai ye define karta hai (MUST HAVE)
* **Recursive Case:** Recursive call with modified parameters
* **Progress Towards Base Case:** Har call se problem smaller honi chahiye

**Base Case Kyu Zaroori Hai:**
* Agar nahi hoga to infinite recursion (stack overflow)
* Program crash ho jayega

---

## Recursion ke Types:

### 1. Linear Recursion
- Function ek bar call hota hai
- Example: Factorial, Linear search

```python
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n-1)  # Recursive case
```

### 2. Binary Recursion
- Function do baar call hota hai
- Example: Fibonacci

```python
def fibonacci(n):
    if n <= 1:  # Base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Two recursive calls
```

### 3. Tail Recursion
- Last statement recursion call hoti hai
- Optimize ho sakta hai (compiler optimization)

---

## Example: Factorial

Recursion Tree:
```
factorial(5)
    = 5 * factorial(4)
    = 5 * 4 * factorial(3)
    = 5 * 4 * 3 * factorial(2)
    = 5 * 4 * 3 * 2 * factorial(1)
    = 5 * 4 * 3 * 2 * 1
    = 120
```

**Time Complexity:** O(n)
**Space Complexity:** O(n) - recursive call stack

---

## Example: Fibonacci

**Inefficient (Naive) Approach:**
```
f(5) = f(4) + f(3)
       = (f(3) + f(2)) + (f(2) + f(1))
       = ((f(2) + f(1)) + (f(1) + f(0))) + ((f(1) + f(0)) + f(1))
```
**Problem:** Same subproblems baar-baar calculate hote hain!

**Time Complexity:** O(2^n) - VERY BAD

**Optimized Approach (Memoization):**
- Already calculated values ko store karo
- Time: O(n), Space: O(n)

---

## Advantages of Recursion:

* Code simple aur readable hota hai
* Natural fit for tree/graph problems
* Divide and conquer problems ke liye perfect

## Disadvantages of Recursion:

* Stack space zyada use hota hai
* Function call overhead
* Deep recursion se stack overflow
* Performance comparatively slow

---

**Viva Line:**
"Recursion when function khud ko call karta hai with base case. Base case MUST HAI nahi to infinite recursion. Tree traversal, factorial, fibonacci me use hota hai."

---

# 🟢 SEARCHING ALGORITHMS

## Linear Search

**Definition:**
Array ke har element ko ek-ek karke target value se compare karte hain.

**Process:**
1. Start from index 0
2. Check if element == target
3. Agar match ho gaya return index
4. Nahi to next element check karo
5. End tak nahi mila to -1 return karo

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

**Characteristics:**
* **Time:** O(n) worst case, Ω(1) best case
* **Space:** O(1) - constant space
* **Works on:** Sorted and unsorted arrays
* **Best for:** Small arrays, linked lists

---

## Binary Search

**Definition:**
Sorted array me middle element compare karte hain aur half part eliminate karte hain.

**Prerequisite:** Array must be SORTED!

**Process:**
1. Find middle element
2. Agar middle == target → return middle index
3. Agar middle < target → right half me search karo
4. Agar middle > target → left half me search karo
5. Repeat until element milti hai ya array khatam

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Example:**
Array: [1, 3, 5, 7, 9, 11]
Target: 7
```
Iteration 1: left=0, right=5, mid=2 (value=5) → 5 < 7, left=3
Iteration 2: left=3, right=5, mid=4 (value=9) → 9 > 7, right=3
Iteration 3: left=3, right=3, mid=3 (value=7) → 7 == 7, return 3
```

**Characteristics:**
* **Time:** O(log n) - very efficient
* **Space:** O(1) or O(log n) recursive
* **Works on:** SORTED arrays only
* **Best for:** Large sorted datasets

**Comparison:**
| Feature | Linear | Binary |
|---------|--------|--------|
| Sorted Required | No | Yes |
| Time Complexity | O(n) | O(log n) |
| Best for | Small/Unsorted | Large/Sorted |

---

# 🟡 SORTING ALGORITHMS

## Bubble Sort (Shalaa Sort)

**Definition:**
Adjacent elements ko compare karte hain aur swap karte hain agar ek dusre ke order me nahi hain.

**Process:**
1. First pass: largest element end me chala jata hai
2. Second pass: second largest backward position me
3. Repeat until sorted

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

**Example:**
Initial: [5, 2, 8, 1, 9]
Pass 1: [2, 5, 1, 8, 9] (9 on place)
Pass 2: [2, 1, 5, 8, 9] (8 on place)
Pass 3: [1, 2, 5, 8, 9] (5 on place)
Pass 4: [1, 2, 5, 8, 9] (done)

**Characteristics:**
* **Time:** O(n²) worst/average, O(n) best (already sorted)
* **Space:** O(1) - in-place sorting
* **Stable:** Yes (equal elements order preserved)
* **Adaptive:** Zyada nahi
* **Use:** Educational purpose, small arrays

---

## Selection Sort

**Definition:**
Unsorted portion se minimum element find karte hain aur sorted portion ke end me place karte hain.

**Process:**
1. Minimum element find karo
2. First position me swap karo
3. Remaining array ke liye repeat
4. Until sorted

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Example:**
Initial: [5, 2, 8, 1, 9]
Step 1: [1, 2, 8, 5, 9] (1 found, swapped)
Step 2: [1, 2, 8, 5, 9] (2 already in place)
Step 3: [1, 2, 5, 8, 9] (5 found, swapped)
Step 4: [1, 2, 5, 8, 9] (done)

**Characteristics:**
* **Time:** O(n²) always
* **Space:** O(1) - in-place
* **Stable:** No (swaps can break order)
* **Use:** When memory is critical

---

## Insertion Sort

**Definition:**
Left side ko sorted rakhte hain aur right side ke elements ko sahi position me insert karte hain.

**Process:**
1. Left side = sorted, Right side = unsorted
2. Right se ek element lo
3. Left me sahi position find karo
4. Sare bade elements ko right me shift karo
5. Element ko insert karo

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```

**Example:**
Initial: [5, 2, 8, 1, 9]
Step 1: [2, 5, 8, 1, 9] (2 insert)
Step 2: [2, 5, 8, 1, 9] (8 already in place)
Step 3: [1, 2, 5, 8, 9] (1 insert)
Step 4: [1, 2, 5, 8, 9] (9 already in place)

**Characteristics:**
* **Time:** O(n²) worst, O(n) best (already sorted)
* **Space:** O(1) - in-place
* **Stable:** Yes
* **Adaptive:** Yes (good for nearly sorted arrays)
* **Use:** Online sorting, small arrays, playing cards analogy

---

## Merge Sort

**Definition:**
Divide & Conquer approach: Array ko half me divide karo, sort karo, phir merge karo.

**Process:**
1. Array ko half me divide karo
2. Recursively left aur right half sort karo
3. Two sorted arrays ko merge karo

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Merge Visualization:**
```
[5, 2, 8, 1, 9]
    /        \
[5, 2]      [8, 1, 9]
  /  \      /    \
[5] [2]  [8]  [1, 9]
       |       /  \
      [2, 5]  [1] [9]
       |      |_____|
      [2, 5]    [1, 9]
       |_________|
        [1, 2, 5, 8, 9]
```

**Characteristics:**
* **Time:** O(n log n) always - very consistent
* **Space:** O(n) - not in-place
* **Stable:** Yes
* **Use:** Large datasets, guaranteed performance, external sorting

---

## Quick Sort (Covered Later if needed)

**Definition:**
Pivot element select karte hain aur partition karte hain.

**Time:** O(n log n) average, O(n²) worst
**Space:** O(log n) recursive

---

**Sorting Comparison Table:**
| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable |
|-----------|------------|-----------|------------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |

---

# 🟡 1D DATA STRUCTURES

## Array

**Definition:**
Fixed-size collection of elements same type ke jo continuous memory me store hote hain.

**Characteristics:**
* **Access Time:** O(1) - very fast
* **Insertion:** O(n) - may need shifting
* **Deletion:** O(n) - may need shifting
* **Memory:** Continuous block
* **Fixed Size:** Zyada data store nahi kar sakte

**Advantages:**
* Fast random access
* Memory efficient
* Cache friendly

**Disadvantages:**
* Fixed size
* Insertion/deletion slow
* Memory waste if not full

---

## List (Dynamic Array)

**Definition:**
Variable-size collection jo dynamically grow ya shrink kar sakta hai (Python me list, Java me ArrayList).

**Characteristics:**
* **Access Time:** O(1)
* **Insertion:** O(n) average
* **Deletion:** O(n) average
* **Dynamic Size:** Automatically resize hota hai
* **Memory:** Array se zyada space use hota hai

**Advantages:**
* Dynamic sizing
* Flexible
* Easy to use

**Disadvantages:**
* Resizing overhead
* Extra memory overhead
* Slower insertion/deletion

---

## Tuple (Immutable)

**Definition:**
Fixed-size collection jisme elements change nahi ho sakte (read-only).

**Characteristics:**
* Immutable - change nahi ho sakta
* Slightly faster than list
* Can be dictionary key (lists cannot)
* Memory efficient

**Use:**
```python
point = (3, 4)  # Immutable
point[0] = 5    # Error!
```

---

## Set

**Definition:**
Unordered collection of unique elements without duplicates.

**Characteristics:**
* **Time (Add):** O(1) average
* **Time (Remove):** O(1) average
* **Time (Search):** O(1) average
* **Duplicates:** Not allowed
* **Order:** Not maintained

**Use:**
* Duplicate removal
* Membership testing
* Mathematical operations (union, intersection)

```python
s = {1, 2, 3, 2}
print(s)  # {1, 2, 3}
```

---

## Dictionary (Hash Map)

**Definition:**
Key-value pairs ka collection jisme key se value fast lookup hoti hai.

**Characteristics:**
* **Time (Lookup):** O(1) average
* **Time (Insert):** O(1) average
* **Time (Delete):** O(1) average
* **Keys:** Unique hone chahiye
* **Values:** Duplicates ho sakti hain

**Use:**
* Fast lookup
* Caching
* Frequency counting
* Mapping data

```python
phone_book = {"Alice": "123-456", "Bob": "987-654"}
print(phone_book["Alice"])  # "123-456" - O(1)
```

---

# 🟡 2D ARRAY (MATRIX)

## Matrix Basics

**Definition:**
2D array jo rows aur columns me data store karta hai.

**Representation:**
```
Matrix 3x3:
    0   1   2
0   1   2   3
1   4   5   6
2   7   8   9
```

**Access:** matrix[row][col]

---

## Common Operations

### 1. Row-wise Traversal
```python
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j])
```
Time: O(rows × cols)

### 2. Column-wise Traversal
```python
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j])
```
Time: O(rows × cols)

### 3. Diagonal Traversal
```python
# Main diagonal
for i in range(min(rows, cols)):
    print(matrix[i][i])
```

### 4. Transpose
Rows ko columns me convert karna

```
Original:     Transpose:
1 2 3         1 4 7
4 5 6   →     2 5 8
7 8 9         3 6 9
```

```python
transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
```

### 5. Spiral Traversal
```
    1 2 3
    8 9 4
    7 6 5

Order: 1,2,3,4,5,6,7,8,9
```

Process:
1. Top row (left to right)
2. Right column (top to bottom)
3. Bottom row (right to left)
4. Left column (bottom to top)
5. Repeat for inner matrix

---

# 🟠 STACK

**Definition:**
Stack ek linear data structure hai jo LIFO (Last In First Out) principle follow karta hai. Last me push kiya gaya element first nikalta hai.

**Visual:**
```
Push 1: [1]
Push 2: [1, 2]
Push 3: [1, 2, 3] ← Top
Pop:    [1, 2]
Pop:    [1]
```

**Main Operations:**

* **push(x):** Element stack ke top par add karo - O(1)
* **pop():** Top element remove karo - O(1)
* **peek() / top():** Top element dekho without removing - O(1)
* **isEmpty():** Check if empty - O(1)
* **size():** Stack me kitne elements hain - O(1)

**Implementation (Using List):**
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
```

**Real World Examples:**
* Browser back button - history stack
* Undo/Redo functionality
* Function call stack (recursion)
* Expression evaluation
* Parentheses matching

**Classic Problem: Balanced Parentheses**
```python
def is_balanced(expr):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expr:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0
```

**Characteristics:**
* **Time:** All operations O(1)
* **Space:** O(n) for n elements
* **Order:** LIFO

---

# 🟠 QUEUE

**Definition:**
Queue ek linear data structure hai jo FIFO (First In First Out) principle follow karta hai. Pehle enter kiya gaya element pehle nikalta hai.

**Visual:**
```
Enqueue 1: [1]
Enqueue 2: [1, 2]
Enqueue 3: [1, 2, 3]
Dequeue:   [2, 3]      ← 1 nikalta hai first
```

**Main Operations:**

* **enqueue(x):** Element rear par add karo - O(1)
* **dequeue():** Front element remove karo - O(1)
* **front():** Front element dekho - O(1)
* **isEmpty():** Check if empty - O(1)
* **size():** Elements count - O(1)

**Implementation (Using List):**
```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, x):
        self.items.append(x)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
    
    def front(self):
        if not self.isEmpty():
            return self.items[0]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
```

**Better Implementation (Using Collections.deque):**
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, x):
        self.items.append(x)
    
    def dequeue(self):
        return self.items.popleft()  # O(1) instead of O(n)
```

**Real World Examples:**
* Printer queue
* Customer service queue (line)
* CPU scheduling
* Breadth-First Search (BFS)
* Traffic signal simulation

**Characteristics:**
* **Time:** All operations O(1) (with deque)
* **Space:** O(n) for n elements
* **Order:** FIFO

---

# 🟠 LINKED LIST

**Definition:**
Nodes ka collection jisme har node data aur next node ka reference (pointer) store karta hai. Continuous memory zaroori nahi hai.

**Node Structure:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

**Visual:**
```
Linked List: 1 → 2 → 3 → None

Node1: [data: 1 | next: •]
Node2: [data: 2 | next: •]
Node3: [data: 3 | next: None]
```

**Main Operations:**

1. **Traversal:** O(n)
```python
curr = head
while curr:
    print(curr.data)
    curr = curr.next
```

2. **Insertion at Beginning:** O(1)
```python
new_node = Node(value)
new_node.next = head
head = new_node
```

3. **Insertion at End:** O(n)
```python
new_node = Node(value)
if not head:
    head = new_node
else:
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
```

4. **Deletion:** O(n)
```python
# Delete node with specific value
if head.data == value:
    head = head.next
else:
    curr = head
    while curr.next:
        if curr.next.data == value:
            curr.next = curr.next.next
            break
        curr = curr.next
```

**Deletion Logic Explanation:**
`prev.next = curr.next` → Current node ko bypass kar dete hain

**Advantages:**
* **Dynamic Size:** Jitna chahiye utna grow kar sakte hain
* **Easy Insertion/Deletion:** Middle me insert/delete kar sakte hain
* **Memory Efficient:** Exact memory use hota hai

**Disadvantages:**
* **No Random Access:** nth element access ke liye traverse karna padta hai O(n)
* **Extra Memory:** Extra pointer ke liye memory chahiye
* **Cache Unfriendly:** Scattered memory locations

**Types of Linked Lists:**
1. **Singly Linked List:** Har node ke next pointer hote hain
2. **Doubly Linked List:** Har node ke prev aur next dono pointers hote hain
3. **Circular Linked List:** Last node first node ko point karta hai

**Comparison:**
| Operation | Linked List | Array |
|-----------|------------|-------|
| Access | O(n) | O(1) |
| Insertion | O(1) (at beginning) | O(n) |
| Deletion | O(1) (if pointer available) | O(n) |
| Space | O(n + pointers) | O(n) |

---

# 🔴 TREE

**Definition:**
Tree ek non-linear data structure hai jo nodes aur edges se banana hota hai. Hierarchical structure hota hai. Kisi root node se start hota hai.

**Tree Terminology:**
* **Root:** Top node (parent nahi hai)
* **Parent:** Node jo dusre node ko point karta hai
* **Child:** Node jo dusre node se point hota hai
* **Leaf:** Node jiske koi child nahi (terminal node)
* **Edge:** Connection between nodes
* **Level:** Root se distance
* **Height:** Longest path from node to leaf
* **Depth:** Root se distance

**Visual:**
```
        A (Root, Height=2)
       / \
      B   C (Internal nodes)
     / \
    D   E (Leaf nodes)

Level 0: A
Level 1: B, C
Level 2: D, E
```

---

## Binary Tree

**Definition:**
Tree jisme har node ke maximum 2 children ho sakte hain (left aur right).

**Visual:**
```
        1
       / \
      2   3
     / \
    4   5
```

**Types:**
1. **Full Binary Tree:** Har node ke 0 ya 2 children hain
2. **Complete Binary Tree:** Sare levels poore hain except last level
3. **Perfect Binary Tree:** Sare levels poore hain
4. **Balanced Binary Tree:** Height difference ≤ 1

**Properties:**
* Maximum nodes at level n = 2^n
* Maximum nodes in tree of height h = 2^h - 1
* Minimum height for n nodes = log(n+1) - 1

---

## Binary Search Tree (BST)

**Definition:**
Binary Tree jisme **Left < Root < Right** property hoti hai.

**Property:**
* Left subtree ke sare nodes root se chhote hote hain
* Right subtree ke sare nodes root se bade hote hain

**Visual:**
```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80
```

**Operations:**
1. **Search:** O(log n) average, O(n) worst
2. **Insertion:** O(log n) average, O(n) worst
3. **Deletion:** O(log n) average, O(n) worst

**Search Algorithm:**
```python
def search(node, value):
    if node is None:
        return False
    if value == node.data:
        return True
    elif value < node.data:
        return search(node.left, value)
    else:
        return search(node.right, value)
```

**Advantages:**
* Efficient searching
* Sorted data
* In-order traversal gives sorted sequence

**Problem:** Unbalanced tree → O(n) operations
**Solution:** AVL Tree, Red-Black Tree (balanced BST)

---

## Tree Traversal

### 1. Breadth-First Search (BFS) - Level Order

**Definition:**
Level by level traverse karte hain (left to right).

**Process:**
1. Queue use karte hain
2. Root enqueue karo
3. While queue not empty:
   - Dequeue करо
   - Process करो
   - Left aur right children enqueue करो

```python
from collections import deque

def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

**Example Tree:**
```
        1
       / \
      2   3
     / \
    4   5

BFS Order: 1, 2, 3, 4, 5 (level by level)
```

**Time:** O(n), **Space:** O(h) where h = height

---

### 2. Depth-First Search (DFS) - Recursive

#### a) Preorder (Root Left Right)

Root → Left Subtree → Right Subtree

```python
def preorder(node):
    if node:
        print(node.data)          # Root
        preorder(node.left)        # Left
        preorder(node.right)       # Right
```

Example: **1, 2, 4, 5, 3**

**Use:** Copy tree, Prefix expression

#### b) Inorder (Left Root Right)

Left Subtree → Root → Right Subtree

```python
def inorder(node):
    if node:
        inorder(node.left)         # Left
        print(node.data)           # Root
        inorder(node.right)        # Right
```

Example: **4, 2, 5, 1, 3**

**Use:** BST me sorted output deta hai!

#### c) Postorder (Left Right Root)

Left Subtree → Right Subtree → Root

```python
def postorder(node):
    if node:
        postorder(node.left)       # Left
        postorder(node.right)      # Right
        print(node.data)           # Root
```

Example: **4, 5, 2, 3, 1**

**Use:** Delete tree, Postfix expression

---

**Traversal Comparison:**
```
        1
       / \
      2   3
     / \
    4   5

Preorder:   1 → 2 → 4 → 5 → 3 (Root first)
Inorder:    4 → 2 → 5 → 1 → 3 (Root middle) ← BST me sorted!
Postorder:  4 → 5 → 2 → 3 → 1 (Root last)
BFS:        1 → 2 → 3 → 4 → 5 (Level-wise)
```

---

# ⚫ GRAPH

**Definition:**
Graph nodes (vertices) aur edges ka collection hai. Tree ka generalized form hai. Cycles possible hain.

**Components:**
* **Vertices (Nodes):** Data points
* **Edges:** Connections between vertices
* **Weight:** Optional, edge ka value

**Visual:**
```
Simple Graph:
    1 --- 2
    |     |
    3 --- 4

Weighted Graph:
    1 -5- 2
    |3   4|
    3 -2- 4
```

---

## Graph Types

### 1. Directed Graph (Digraph)

Edges ka direction hota hai (A → B)

```
    1 → 2
    ↓   ↓
    3 → 4
```

### 2. Undirected Graph

Edges do-taraf chalte hain (A ↔ B)

```
    1 --- 2
    |     |
    3 --- 4
```

### 3. Weighted Graph

Har edge ka weight hota hai

```
    1 -5- 2
    |-3- 4
```

### 4. Cyclic Graph

Cycle hoti hai (koi node se start karke wahin par aa sakte hain)

### 5. Acyclic Graph (DAG - Directed Acyclic Graph)

Koi cycle nahi hoti

---

## Graph Representation

### 1. Adjacency Matrix

```
     0  1  2  3
   +--+--+--+--+
0  | 0| 1| 1| 0|
1  | 1| 0| 1| 1|
2  | 1| 1| 0| 1|
3  | 0| 1| 1| 0|
```

* **Space:** O(V²)
* **Edge Lookup:** O(1)
* **Use:** Dense graphs

### 2. Adjacency List

```
0: [1, 2]
1: [0, 2, 3]
2: [0, 1, 3]
3: [1, 2]
```

* **Space:** O(V + E)
* **Edge Lookup:** O(degree)
* **Use:** Sparse graphs

---

## Graph Traversal

### 1. Breadth-First Search (BFS)

Level-by-level traverse करते हैं। Queue use करते हैं।

```python
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**Time:** O(V + E), **Space:** O(V)

**Use:**
* Shortest path in unweighted graph
* Level-order traversal
* Connected components

---

### 2. Depth-First Search (DFS)

Depth me jaate hain। Stack या recursion use करते हैं।

```python
def dfs_recursive(graph, vertex, visited):
    visited.add(vertex)
    print(vertex)
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Usage
visited = set()
dfs_recursive(graph, 0, visited)
```

**Iterative DFS:**
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(graph[vertex])
```

**Time:** O(V + E), **Space:** O(V)

**Use:**
* Topological sorting
* Cycle detection
* Connected components
* Strongly connected components

---

**Comparison:**
| Feature | BFS | DFS |
|---------|-----|-----|
| Data Structure | Queue | Stack/Recursion |
| Order | Level-wise | Depth-wise |
| Memory | More (wide tree) | Less (deep tree) |
| Shortest Path | Yes | No |
| Cycle Detection | Yes | Yes |

---

# 🔥 FINAL KEY CONCEPTS (VIVA SAVER)

**Master Line:**
"Data structures data ko organize aur manage karte hain. Algorithms us data ko efficiently process karte hain. Sahi combination se problem solve hota hai."

**Quick Cheat Sheet:**

**Time Complexities:**
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n) < O(n!)
```

**Data Structure Operations:**
```
Array: Access=O(1), Insert/Delete=O(n)
Linked List: Access=O(n), Insert/Delete=O(1)
Stack/Queue: Push/Pop=O(1)
BST: Search/Insert/Delete=O(log n) average
Graph: BFS/DFS=O(V+E)
```

**When to Use What:**
* **Fast Access?** Array
* **Fast Insertion/Deletion?** Linked List, Stack, Queue
* **Sorted Data?** BST, Sorted Array
* **Unique Elements?** Set, HashMap
* **Key-Value Pairs?** Dictionary/HashMap
* **Hierarchical Data?** Tree, Graph
* **Level-wise Traversal?** BFS, Queue
* **Depth Traversal?** DFS, Stack

**Common Interview Questions:**
1. Array reverse करो
2. Linked list me cycle detect करो
3. Tree को traverse करो (all 4 ways)
4. Graph में shortest path खोजो (BFS)
5. Balanced parentheses check करो (Stack)
6. Two sum problem (HashMap)
7. Merge sorted arrays (Merge Sort concept)
8. Fibonacci with memoization
9. Invert binary tree
10. Valid BST check

**Red Flags (Wrong Answers):**
* Recursion without base case = infinite recursion ❌
* Confused Big O with actual time ❌
* Stack vs Queue operations mixed ❌
* Forgetting LIFO/FIFO ❌
* Thinking array/linked list are equivalent ❌

---

# 🎯 FINAL VIVA LINES (MEMORIZE THESE)

1. "Algorithm ek systematic step-by-step procedure hai problem solve karne ka."

2. "Big O worst case, Omega best case, Theta average case batata hai."

3. "Recursion = function khud ko call karta hai with base case to avoid infinite recursion."

4. "Binary search O(log n) me kaam karta hai kyunki har time half data eliminate hota hai।"

5. "Stack LIFO follow karta hai - last enter, first exit. Example: browser back button."

6. "Queue FIFO follow karta hai - first enter, first exit. Example: customer line."

7. "Linked List dynamic hota hai but random access nahi kar sakte - O(n) traverse karna padta hai."

8. "Tree = hierarchical structure जहाँ root se start करते हैं। BST में Left < Root < Right।"

9. "Graph = nodes और edges का collection। BFS queue use करता है, DFS stack।"

10. "Data structures = data organize करते हैं। Algorithms = efficiently process करते हैं।"

---

This is a comprehensive guide for DSA interview preparation. Isko memorize करो aur confidence se bolna! 💪
