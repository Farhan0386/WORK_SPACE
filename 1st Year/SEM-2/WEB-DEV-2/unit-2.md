# UNIT 2 – ASYNCHRONOUS JS

## 1. Synchronous vs Asynchronous

### Synchronous:
- Executes line by line

Example:
console.log("A")
console.log("B")

### Asynchronous:
- Executes later

Example:
setTimeout(() => console.log("A"), 1000)
console.log("B")

Output:
B
A

---

## 2. setTimeout & setInterval

### setTimeout
Runs once after delay

setTimeout(() => {
  console.log("Hello")
}, 1000)

### setInterval
Runs repeatedly

setInterval(() => {
  console.log("Hi")
}, 1000)

---

## 3. Event Loop (VERY IMPORTANT)

### Components:
- Call Stack
- Web APIs
- Callback Queue
- Event Loop

### Flow:
1. Code goes to call stack
2. Async tasks go to Web APIs
3. After completion → callback queue
4. Event loop pushes to stack

---

## 4. Microtask vs Macrotask

### Microtask:
- Promise.then()

### Macrotask:
- setTimeout()

Priority:
Microtask > Macrotask

---

## 5. Async / Await

### Definition:
Simplified way to handle promises

### Example:
async function getData() {
  const res = await fetch(url)
  const data = await res.json()
  console.log(data)
}

---

## 6. Error Handling

try {
  let a = 10
} catch(err) {
  console.log(err)
}

---

## 7. Fetch API

### GET:
fetch(url)

### POST:
fetch(url, {
  method: "POST",
  body: JSON.stringify(data)
})