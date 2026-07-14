# 🐍 Python Functions – Args, Kwargs, Docstrings, Type Hints

## 🔹 Arguments

- **Positional** → Passed in order of parameters.  

  ```python
  def nameAge(name, age): print(name, age)
  nameAge("Prince", 20)   # Correct
  nameAge(20, "Prince")   # Wrong order
  ```

- **Keyword** → Passed using parameter names (order doesn’t matter).  

  ```python
  nameAge(name="Prince", age=20)
  nameAge(age=20, name="Prince")
  ```

## 🔹 *args and **kwargs

- `*args` → Collects variable-length positional arguments (tuple).  

  ```python
  def myFun(*args): print(args)
  myFun("Hello", "World")  # ('Hello', 'World')
  ```

- `**kwargs` → Collects variable-length keyword arguments (dict).  

  ```python
  def myFun(**kwargs): print(kwargs)
  myFun(a=1, b=2)  # {'a': 1, 'b': 2}
  ```

- Both together:

  ```python
  def mix(*args, **kwargs): print(args, kwargs)
  mix(1,2,3, a=4, b=5)
  ```

## 🔹 Docstrings

- Documentation for functions/classes/modules using triple quotes.
- Access via `__doc__` or `help()`.
- **Single-line**:  

  ```python
  def add(a,b): """Return sum."""; return a+b
  ```

- **Multi-line**:  

  ```python
  def add_numbers(a,b):
      """
      Add two numbers.
      Params: a (int), b (int)
      Returns: int
      """
      return a+b
  ```

## 🔹 Type Hints

- Annotate expected types for clarity and static checking.

  ```python
  age: int = 25
  def greet(name: str) -> str: return f"Hello, {name}"
  def add(x: int, y: int) -> int: return x+y
  ```

- Collections & Optional:  

  ```python
  from typing import Optional, List, Tuple
  def get_user(id: int) -> Optional[str]: ...
  def sum_numbers(nums: List[int]) -> int: ...
  def get_name_and_age() -> Tuple[str,int]: ...
  ```

---
✅ Quick Review:

- Positional vs Keyword args → order vs names  
- `*args` / `**kwargs` → flexible arguments  
- Docstrings → documentation inside code  
- Type hints → improve readability & catch errors
