# 🐍 Python Functions – Quick Notes

## 🔹 What is a Function?

- Block of reusable code for a single task.
- Improves modularity, readability, and reusability.

## 🔹 Types

1. Built-in → `print()`, `len()`
2. Module functions → `math.sqrt()`
3. User-defined → `def my_func():`

## 🔹 Key Points

- Defined with `def` keyword.
- Parameters can have default values.
- Use `return` to send back results (default: `None`).
- Variables inside functions are local (scope).

## 🔹 Examples

```python
def greet():
    print("Hello!")

def add(a, b):
    return a + b

print(add(5, 3))  # 8
```

## 🔹 Special Functions

- **Recursive** → factorial
- **Lambda** → `lambda x: x*x`
- **Nested** → functions inside functions

## 🔹 Practice Ideas

- Check if list contains element
- Concatenate strings
- Count vowels in a string
- Sum numbers in a range
