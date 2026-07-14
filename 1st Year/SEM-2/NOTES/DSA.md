# DSA - Theory Notes (Units 1–4)

> Concise, exam-oriented notes: definitions, explanations, diagrams, complexity, advantages, disadvantages, applications, and estimated exam weight.

---

**UNIT 1 — Foundations & Algorithmic Analysis**

## Algorithm — Definition (2 Marks)
- **Definition:** An ordered, finite set of well-defined steps to solve a problem (input → steps → output).
- **Key Points:** correctness, finiteness, definiteness, input/output, generality.
- **Diagram:** Input --> [Step1] --> [Step2] --> ... --> Output
- **Applications:** All computing tasks.
- **Conclusion:** Foundation of program design and analysis.

## Characteristics of an Algorithm (2 Marks)
- **Correctness:** Produces expected output for all valid inputs.
- **Finiteness:** Terminates after finite steps.
- **Determinism:** Steps precisely defined.
- **Generality:** Works for all inputs in domain.
- **Efficiency & Robustness.**

## Data Structures and ADT (5 Marks)
- **Data Structure:** Concrete memory organization (array, list, tree).
- **ADT (Abstract Data Type):** Logical model + operations (e.g., `Stack` with `push`/`pop`).
- **Key Idea:** ADT = interface; data structure = implementation.

## Time Complexity (Very Important)
- **Definition:** Number of basic operations as a function of input size `n`.
- **Key Points:** Analyze asymptotically; ignore constants and lower-order terms.

## Space Complexity (Very Important)
- **Definition:** Amount of memory required by algorithm as function of `n`.
- **Key Points:** Distinguish input space vs auxiliary space; in-place = O(1) extra.

## Big-O Notation (Very Important)
- **Definition:** Upper bound on growth (worst-case). `f(n)=O(g(n))` means f ≤ c·g for large n.
- **Common Classes:** O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n).

## Omega Notation (Ω) (5 Marks)
- **Definition:** Lower bound on growth (best-case). `f(n)=Ω(g(n))`.

## Theta Notation (Θ) (Very Important)
- **Definition:** Tight bound; f = Θ(g) if f = O(g) and f = Ω(g).

## Best, Average, Worst Case (5 Marks)
- **Definitions:** Scenarios describing minimal, expected, maximal cost.
- **Example:** Linear search best O(1), worst O(n).

## Complexity Comparison (Very Important)
- **Order (small→large):** O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)

## Recursion (Very Important)
- **Definition:** Function calls itself on smaller input.
- **Key Parts:** Base case, recursive call(s), recursion depth.
- **Advantages:** Natural for divide-and-conquer and tree problems.
- **Disadvantages:** Call overhead, stack usage, risk of overflow.
- **Diagram:** f(n) -> f(n-1) -> f(n-2) -> ... -> base case

### Base Case (2 Marks)
- **Definition:** Condition where recursion stops and returns directly.

### Recursive Calls (2 Marks)
- **Definition:** Points where function invokes itself; number of calls defines complexity via recurrence relations.

### Call Stack (Very Important)
- **Definition:** Stack of activation records (locals + return address). Each recursive call pushes a frame.
- **Space:** O(max recursion depth).

### Factorial using Recursion (Theory only, 2 Marks)
- **Relation:** n! = n × (n-1)!, base 0! = 1.
- **Time:** T(n) = T(n-1) + O(1) ⇒ O(n). Space O(n) for call stack.

### Fibonacci using Recursion (Theory only, 2 Marks)
- **Relation:** F(n) = F(n-1) + F(n-2), F(0)=0, F(1)=1.
- **Naïve time:** Exponential O(φ^n). Use DP/memoization to achieve O(n).

## Recursion vs Iteration (Very Important)
- **Recursion:** Cleaner for recursive structures, uses call stack, possible overhead.
- **Iteration:** Loop-based, space/time efficient for linear processes.

## Divide and Conquer (Very Important)
- **Definition:** Split problem into subproblems, solve recursively, combine results.
- **Recurrence:** T(n)=a T(n/b) + f(n). Use Master Theorem for solution.
- **Examples:** Merge sort, quicksort, binary search.

## Greedy Method (Very Important)
- **Definition:** Make locally optimal choices hoping for global optimum.
- **Condition to work:** Greedy-choice property + optimal substructure.
- **Examples:** Activity selection, Huffman coding, Prim/Kruskal (MST).

## Dynamic Programming (Very Important)
- **Definition:** Optimize using overlapping subproblems + memoization/tabulation.
- **Approaches:** Top-down (memoization) and bottom-up (tabulation).
- **Examples:** Knapsack, edit distance, DP Fibonacci.

---

**UNIT 2 — Linear Data Structures**

## Arrays (Very Important)
- **Definition:** Contiguous block of memory storing same-type elements.
- **Key Points:** O(1) random access, insert/delete O(n) due to shifts.
- **Advantages:** Cache-friendly, simple.
- **Disadvantages:** Fixed size (static), expensive mid-array modifications.
- **Applications:** Lookup tables, buffers.

### 1D Arrays (2 Marks)
- Traverse O(n), search O(n), update O(1).

### 2D Arrays / Matrix (5 Marks)
- **Definition:** Grid with rows × columns. Access `A[i][j]` O(1).
- **Transpose:** Swap `A[i][j]` with `A[j][i]` (square matrix in-place).
- **Spiral Traversal:** Use four boundaries (top, bottom, left, right). Complexity O(mn).

## List / Tuple / Set / Dictionary (Conceptual, 2–5 Marks)
- **List:** Ordered, mutable.
- **Tuple:** Ordered, immutable.
- **Set:** Unordered, unique elements; average O(1) membership.
- **Dictionary (Map):** Key-value store; average O(1) access with hashing.

## Linked List (Very Important)
- **Definition:** Nodes with `data` + pointer(s); dynamic, non-contiguous.
- **Singly:** `data | next` — one-directional.
- **Doubly:** `prev | data | next` — bidirectional.
- **Circular:** Last node points to head.
- **Complexities:** Access O(n), insert/delete at known node O(1).
- **Advantages:** Dynamic size, cheap insertion/deletion.
- **Disadvantages:** Extra pointer memory, poor cache locality.

## Stack (LIFO) — ADT (Very Important)
- **Ops:** `push`, `pop`, `peek`.
- **Impl.:** Array or linked list. Complexity push/pop O(1).
- **Applications:** Function call stack, expression evaluation, backtracking.

## Queue (FIFO) — ADT (Very Important)
- **Ops:** `enqueue`, `dequeue`, `front`.
- **Impl.:** Circular array or linked list. Complexity O(1).
- **Applications:** Scheduling, BFS, buffering.

---

**UNIT 3 — Searching & Sorting Algorithms (MOST IMPORTANT)**

For each algorithm: Definition · Working principle · Steps · Time/Space · Advantages · Disadvantages · Applications.

## Searching

### Linear Search (Very Important)
- **Definition:** Check elements sequentially.
- **Time:** Best O(1), Avg/Worst O(n). Space O(1).
- **Use:** Unsorted arrays or small lists.

### Binary Search (Very Important)
- **Definition:** Repeatedly halve sorted array.
- **Time:** O(log n) average/worst, O(1) space iterative.
- **Requirement:** Data must be sorted.

## Sorting Concepts
- **Stable vs Unstable:** Stable preserves equal-key order.
- **In-place vs Out-place:** In-place uses O(1) extra space.

### Bubble Sort (5–8 Marks)
- **Idea:** Repeated adjacent swaps; largest bubbles to end.
- **Time:** Best O(n) (with check), Avg/Worst O(n^2). Space O(1). Stable, in-place.

### Selection Sort (5 Marks)
- **Idea:** Select minimum and swap into place each pass.
- **Time:** O(n^2) all cases. Space O(1). Not stable by default.

### Insertion Sort (5–8 Marks)
- **Idea:** Build sorted prefix by inserting items into correct position.
- **Time:** Best O(n), Avg/Worst O(n^2). Space O(1). Stable, good for nearly-sorted arrays.

### Merge Sort (Very Important)
- **Idea:** Divide, sort halves, merge.
- **Time:** O(n log n) all cases. Space O(n). Stable, out-place.

### Quick Sort (Very Important)
- **Idea:** Partition around pivot, recurse.
- **Time:** Avg O(n log n), Worst O(n^2) (bad pivot). Space O(log n) average. In-place, not stable.

### Heap Sort (5–8 Marks)
- **Idea:** Build heap, repeatedly extract max/min.
- **Time:** O(n log n) all cases. Space O(1). In-place, not stable.

### Counting Sort (5 Marks)
- **Idea:** Count occurrences, compute positions.
- **Time:** O(n + k), Space O(k). Stable if implemented so. Works for small integer ranges.

### Radix Sort (5–8 Marks)
- **Idea:** Sort by digits using stable sort (e.g., counting). For fixed digit size, O(n).

## Sorting Complexity Table (quick)
- Bubble: Best O(n), Avg/Worst O(n^2), Space O(1), Stable: Yes
- Selection: O(n^2), Space O(1), Stable: No
- Insertion: Best O(n), Avg/Worst O(n^2), Space O(1), Stable: Yes
- Merge: O(n log n), Space O(n), Stable: Yes
- Quick: Avg O(n log n), Worst O(n^2), Space O(log n), Stable: No
- Heap: O(n log n), Space O(1), Stable: No
- Counting: O(n+k), Space O(k), Stable: Yes
- Radix: O(d(n+k)), Space O(n+k), Stable: Yes

---

**UNIT 4 — Trees, Graphs & Advanced Data Structures**

## Tree (Very Important)
- **Definition:** Hierarchical nodes connected by edges; no cycles.
- **Terminology:** root, parent, child, leaf, internal node, depth, height.

## Binary Tree (Very Important)
- **Definition:** Each node has ≤ 2 children (left, right).
- **Types:** Full, complete, perfect, balanced, skewed.

## Binary Search Tree (BST) (Very Important)
- **Property:** Left subtree keys < node key < right subtree keys.
- **Ops:** Search/Insert/Delete — Average O(log n), Worst O(n) if skewed.

## Tree Traversals (Very Important)
- **Preorder:** root → left → right (use for copy/prefix).
- **Inorder:** left → root → right (BST yields sorted order).
- **Postorder:** left → right → root (use for delete/postfix eval).
- **Level-order:** BFS using queue (visit level by level).
- **Complexity:** O(n) time for all traversals.

## Heap (Very Important)
- **Definition:** Complete binary tree with heap property (max or min).
- **Array index:** left=2i+1, right=2i+2, parent=(i-1)/2.
- **Ops:** build O(n), insert/extract O(log n).

## Graph (Very Important)
- **Definition:** (V, E) with vertices and edges; can be directed/undirected, weighted/unweighted.
- **Types:** Directed, undirected, cyclic, acyclic, connected, disconnected.

## Graph Representation
- **Adjacency Matrix:** V×V matrix. Space O(V^2). Edge check O(1).
- **Adjacency List:** List per vertex. Space O(V + E). Efficient neighbor iteration.
- **Use:** Use list for sparse graphs, matrix for dense graphs.

## BFS (Very Important)
- **Idea:** Level-order graph traversal using queue; finds shortest path in unweighted graphs.
- **Complexity:** O(V + E) time, O(V) space.

## DFS (Very Important)
- **Idea:** Explore deep before backtracking using recursion/stack.
- **Complexity:** O(V + E) time, O(V) recursion stack worst.

## Hashing (Very Important)
- **Idea:** Map keys to indices using hash function; average O(1) operations.
- **Load factor:** α = n / m (n entries, m buckets).

### Collision Resolution
- **Chaining:** Buckets with lists — simple, good for variable load.
- **Open Addressing:** Linear probing, quadratic probing, double hashing — store in table.

## Tries (Important)
- **Definition:** Prefix tree where edges represent characters.
- **Complexity:** Search/insert O(L) (L = key length). Useful for autocomplete.

## AVL & Red-Black Trees (Less Important)
- **AVL:** Height-balanced BST with balance factor ∈ {-1,0,1}. Ops O(log n).
- **Red-Black:** Color-based balancing guaranteeing O(log n) operations; used in many libraries.

## Other Advanced Structures (Brief)
- **B-Tree:** Balanced multi-way tree for disks/databases.
- **Bloom Filter:** Probabilistic membership (false positives possible).
- **Segment Tree / Fenwick Tree:** Range queries and updates (O(log n)).
- **Skip List:** Probabilistic balanced structure; expected O(log n).
- **KD-Tree / Quad-Tree:** Spatial indexing.

---

**VERY IMPORTANT DIFFERENCE QUESTIONS (Quick tables)**
- Big O vs Omega vs Theta: Upper vs lower vs tight bounds.
- Recursion vs Iteration: Stack vs loop; use-case differences.
- Array vs Linked List: Random access vs dynamic insert/delete.
- Stack vs Queue: LIFO vs FIFO.
- Linear vs Binary Search: Sorted requirement, complexity.
- Bubble vs Selection vs Insertion: swap/selection/insertion strategies.
- Merge vs Quick Sort: space and worst-case trade-offs.
- BFS vs DFS: queue vs stack, shortest-path vs deep exploration.
- Tree vs Graph: tree = acyclic connected graph; graph general.
- Adjacency Matrix vs List: space and neighbor iteration trade-offs.

---

## Study Tips & Conclusion
- **Unit 1:** Master asymptotic notation, recurrence solving, recursion basics.
- **Unit 2:** Memorize operations/complexities of arrays, lists, stacks, queues.
- **Unit 3:** Understand sorting principles, stability, and compare complexities.
- **Unit 4:** Practice traversals (BFS/DFS) and graph representations; memorize heap/hash basics.

If you want, I can now:
- Create a 1-page cheat-sheet per unit, or
- Generate sample 2/5/8-mark answers formatted for exams.

---

*Notes prepared for quick exam revision — concise and structured.*

---

## Code Examples (Concise & Exam-friendly)
> Short Python snippets illustrating key concepts. Keep as reference — focus on theory in exams.

### Recursion — Factorial (Time O(n), Space O(n))
```python
def fact(n):
	if n <= 1:
		return 1
	return n * fact(n-1)
```

### Recursion — Fibonacci (naïve and memoized)
```python
def fib_rec(n):
	if n < 2: return n
	return fib_rec(n-1) + fib_rec(n-2)   # Exponential time

from functools import lru_cache
@lru_cache(None)
def fib_memo(n):
	if n < 2: return n
	return fib_memo(n-1) + fib_memo(n-2)  # O(n) time with memo
```

### Searching — Linear & Binary Search
```python
def linear_search(arr, x):
	for i, v in enumerate(arr):
		if v == x: return i
	return -1   # O(n)

def binary_search(arr, x):
	lo, hi = 0, len(arr)-1
	while lo <= hi:
		mid = (lo + hi) // 2
		if arr[mid] == x: return mid
		if arr[mid] < x: lo = mid + 1
		else: hi = mid - 1
	return -1   # O(log n), requires sorted arr
```

### Simple Sorting — Bubble, Selection, Insertion (short)
```python
def bubble_sort(a):
	n = len(a)
	for i in range(n):
		swapped = False
		for j in range(0, n-i-1):
			if a[j] > a[j+1]: a[j], a[j+1] = a[j+1], a[j]; swapped = True
		if not swapped: break  # O(n^2) worst

def selection_sort(a):
	for i in range(len(a)):
		m = i
		for j in range(i+1, len(a)):
			if a[j] < a[m]: m = j
		a[i], a[m] = a[m], a[i]

def insertion_sort(a):
	for i in range(1, len(a)):
		key = a[i]; j = i-1
		while j >= 0 and a[j] > key:
			a[j+1] = a[j]; j -= 1
		a[j+1] = key
```

### Merge Sort & Quick Sort (concise)
```python
def merge_sort(a):
	if len(a) <= 1: return a
	m = len(a)//2
	L, R = merge_sort(a[:m]), merge_sort(a[m:])
	i = j = 0; res = []
	while i < len(L) and j < len(R):
		if L[i] <= R[j]: res.append(L[i]); i+=1
		else: res.append(R[j]); j+=1
	res.extend(L[i:]); res.extend(R[j:]); return res  # O(n log n)

def quick_sort(a):
	if len(a) <= 1: return a
	p = a[len(a)//2]
	left = [x for x in a if x < p]
	mid  = [x for x in a if x == p]
	right= [x for x in a if x > p]
	return quick_sort(left) + mid + quick_sort(right)  # avg O(n log n)
```

### Stack & Queue (using Python builtins)
```python
# Stack using list
stack = []
stack.append(10)   # push
val = stack.pop()  # pop

# Queue using deque
from collections import deque
q = deque()
q.append(1)        # enqueue
q.popleft()        # dequeue  (O(1))
```

### Singly Linked List — minimal (insert at head)
```python
class Node:
	def __init__(self, v, nxt=None):
		self.v = v; self.nxt = nxt

head = None
def insert_head(val):
	global head
	head = Node(val, head)  # O(1)
```

### Binary Tree — Inorder Traversal (recursive)
```python
class TNode:
	def __init__(self, v, left=None, right=None):
		self.v, self.left, self.right = v, left, right

def inorder(root):
	if not root: return
	inorder(root.left)
	print(root.v)
	inorder(root.right)   # O(n)
```

### Graph Traversals — BFS & DFS (adjacency list)
```python
from collections import deque
def bfs(adj, s):
	vis = set([s]); q = deque([s])
	while q:
		u = q.popleft(); print(u)
		for v in adj[u]:
			if v not in vis: vis.add(v); q.append(v)

def dfs(adj, s, vis=None):
	if vis is None: vis = set()
	vis.add(s); print(s)
	for v in adj[s]:
		if v not in vis: dfs(adj, v, vis)
```

### Hashing — Python dict example (average O(1))
```python
table = {}
table['key'] = 42    # insert O(1)
v = table.get('key') # lookup O(1)
```

---

*These examples are intentionally short — use them as memory aids. Ask to expand any snippet or convert to C/Java.*
