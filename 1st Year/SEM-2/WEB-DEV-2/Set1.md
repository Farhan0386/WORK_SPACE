# SET 1 & SET 2 – REACT PRACTICAL NOTES

------------------------------------
SET 1 – Q1: PROPS (Parent → Child)
------------------------------------

## Code

// Child.jsx
function Child(props) {
  return (
    <div>
      <h2>{props.name}</h2>
      <h2>{props.age}</h2>
    </div>
  );
}
export default Child;


// App.jsx (Parent)
import Child from "./components/Child";

function App() {
  const name = "Farhan";
  const age = 20;

  return <Child name={name} age={age} />;
}

export default App;


## Syntax Explanation

function Child(props)
- props = object containing data from parent

props.name
- accessing value from props object

<Child name={name} age={age} />
- passing data as attributes

Internally:
props = { name: "Farhan", age: 20 }

## Flow

Parent → sends props → Child receives → displays

------------------------------------
SET 1 – Q2: FETCH API
------------------------------------

## Code

import { useEffect, useState } from "react";

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div>
      {users.map(user => (
        <div key={user.id}>
          <p>{user.username}</p>
          <p>{user.email}</p>
        </div>
      ))}
    </div>
  );
}

export default Users;


## Syntax Explanation

useState([])
- creates state variable (array)

setUsers(data)
- updates state → triggers re-render

useEffect(() => {}, [])
- runs once when component loads

fetch(url)
- calls API

.then(res => res.json())
- converts response to JSON

users.map(...)
- loops through array

key={user.id}
- unique key required by React

## Flow

Component load → useEffect runs → fetch API → store data → display

------------------------------------
SET 2 – Q1: COUNTER
------------------------------------

## Code

import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>{count}</h2>

      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}

export default Counter;


## Syntax Explanation

useState(0)
- initial value = 0

count
- current state value

setCount()
- updates state

onClick={() => setCount(count + 1)}
- arrow function triggered on click

{count}
- display value

## Flow

Click → setCount() → state update → re-render → new value shown

------------------------------------
SET 2 – Q2: CONTEXT API
------------------------------------

## Step 1: Create Context

import { createContext } from "react";
export const MyContext = createContext();

## Step 2: Provide Data (App.jsx)

import { MyContext } from "./context";
import Child from "./components/Child";

function App() {
  return (
    <MyContext.Provider value="Hello from Context">
      <Child />
    </MyContext.Provider>
  );
}

export default App;

## Step 3: Consume Data (Child.jsx)

import { useContext } from "react";
import { MyContext } from "../context";

function Child() {
  const data = useContext(MyContext);

  return <h2>{data}</h2>;
}

export default Child;


## Syntax Explanation

createContext()
- creates global data container

<MyContext.Provider value="Hello">
- provides data

useContext(MyContext)
- consumes data

value="Hello"
- data being shared

## Flow

createContext → Provider sends data → Child uses useContext → data received

------------------------------------
FINAL SUMMARY
------------------------------------

Props → parent to child data  
State → dynamic data  
useEffect → API / side effects  
map → display list  
Context → global data
