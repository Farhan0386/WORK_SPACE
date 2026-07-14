# 📘 README: Python Control Structures – Session 13

🗂️ Unit Overview
This session focuses on Python’s control structures, emphasizing conditional logic patterns including nested and multi-way branching.

🧩 Topics Covered
✅ Recap of Conditional Statements

- If Statement: Executes a block of code if a specified condition is true.
- If-Else Statement: Executes one block if the condition is true, another if false.

🔁 Nested Conditional Statements

- Definition: An if statement placed inside another if statement.
- Use Case: When multiple dependent conditions need to be evaluated.
- Syntax Structure:
if outer_condition:
    if inner_condition:
        # inner if block
    else:
        # inner else block
else:

outer else block

- Key Point: Indentation is the only way to differentiate levels of nesting.

🧪 Nested Conditional Exercises

- Determine if a number is positive, negative, or zero. If positive, check if it’s even or odd.
- Find the largest among three integers. If multiple values are equally the largest, indicate that.

🔀 Multi-way Branching

- Purpose: To evaluate multiple conditions sequentially.
- Structure: Uses if, elif, and else blocks.
- Syntax Pattern:
if condition_1:

 block 1
elif condition_2:
    # block 2
elif condition_3:
    # block 3
else:
    # fallback block

🧪 Multi-way Branching Exercises

- Determine if a number is positive, negative, or zero.
- Grade calculation based on score:
- A: 90–100
- B: 80–89
- C: 70–79
- D: 60–69
- F: 0–59
- Leap year checker:
- Divisible by 4
- Not divisible by 100 unless also divisible by 400
- Month-day calculator:
- Input: Month number (1–12)
- Output: Number of days (assume February has 28 days)
- Find the largest among three integers.

🧾 Final Review

- If Statement: Executes when condition is true.
- If-Else Statement: Executes one of two blocks based on condition.
- If-Elif-Else Statement: Checks multiple conditions in sequence.
- Nested Conditional Statements: Enables complex decision-making by embedding conditions.
