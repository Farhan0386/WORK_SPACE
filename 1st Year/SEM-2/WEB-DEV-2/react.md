# REACT

## 1. What is React?

### Definition:
A JavaScript library used to build UI using components.

---

## 2. Virtual DOM

### Definition:
A lightweight copy of real DOM

### Why:
- Faster updates
- Efficient rendering

---

## 3. JSX

### Definition:
HTML inside JavaScript

Example:
const element = <h1>Hello</h1>

---

## 4. Components

### Functional Component:
function App() {
  return <h1>Hello</h1>
}

---

## 5. Props

### Definition:
Data passed from parent to child

Example:
<Child name="Farhan" />

function Child(props) {
  return <h1>{props.name}</h1>
}

---

## 6. useState (VERY IMPORTANT)

### Definition:
Stores dynamic data

Example:
const [count, setCount] = useState(0)

---

## 7. useEffect

### Definition:
Handles side effects (API, timers)

Example:
useEffect(() => {
  fetch(url)
}, [])

---

## 8. Context API

### Definition:
Global data sharing

### Steps:
- createContext()
- Provider
- useContext()

---

## 9. Routing

### Definition:
Switch pages without reload

Example:
<Route path="/" element={<Home />} />

---

## 10. Forms

### Controlled:
Using state

<input onChange={(e)=>setName(e.target.value)} />

### Uncontrolled:
Using DOM

---

## 11. Lifecycle

Mount → Update → Unmount

(useEffect represents lifecycle)

---

## 12. Props vs State

| Props | State |
|------|------|
| Read-only | Changeable |
| Parent → child | Inside component |