# UNIT 1 – DOM

## 1. DOM (Document Object Model)

### Definition:
DOM is a programming interface that represents HTML as a tree structure so JavaScript can access and modify it.

### Example:
HTML:
<div id="demo">Hello</div>

JS:
document.getElementById("demo").innerText = "Hi";

### Explanation:
- Browser converts HTML → DOM tree
- JS modifies DOM → UI updates

---

## 2. DOM vs HTML

| HTML | DOM |
|------|-----|
| Static | Dynamic |
| Written by developer | Created by browser |
| Cannot change itself | Can be modified using JS |

---

## 3. Selecting Elements

### getElementById
document.getElementById("id")

### getElementsByClassName
document.getElementsByClassName("class")

### querySelector
document.querySelector(".class")

### querySelectorAll
document.querySelectorAll(".class")

---

## 4. classList

### Methods:
element.classList.add("red")
element.classList.remove("red")
element.classList.toggle("red")

### Example:
btn.classList.toggle("active")

---

## 5. Event Handling

### Definition:
Events = user actions (click, input, submit)

### Example:
button.onclick = function() {
  alert("Clicked");
}

---

## 6. Event Bubbling & Capturing

### Bubbling:
Child → Parent

### Capturing:
Parent → Child

---

## 7. preventDefault()

### Definition:
Stops default behavior

### Example:
form.addEventListener("submit", (e) => {
  e.preventDefault();
});

---

## 8. Execution Context (VERY IMPORTANT)

### Definition:
Environment where JS code runs

### Phases:
1. Memory creation
2. Code execution