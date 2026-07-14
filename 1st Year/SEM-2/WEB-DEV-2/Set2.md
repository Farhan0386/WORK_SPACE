# SET 3 & SET 4 – REACT PRACTICAL NOTES

------------------------------------
SET 3 – Q1: FORM (LIVE INPUT UPDATE)
------------------------------------

## Code

import { useState } from "react";

function Form() {
  const [name, setName] = useState("");

  return (
    <div>
      <input
        type="text"
        onChange={(e) => setName(e.target.value)}
      />

      <h2>{name}</h2>
    </div>
  );
}

export default Form;


## Syntax Explanation

useState("")
- initial value = empty string

name
- stores current input value

setName()
- updates value

onChange={(e) => setName(e.target.value)}
- event triggers when user types
- e.target.value = input value

{name}
- displays updated value

## Flow

User types → onChange triggers → setName updates → re-render → value shown

------------------------------------
SET 3 – Q2: ROUTING
------------------------------------

## Install

npm install react-router-dom

## Code

import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

function Home() {
  return <h2>Home</h2>;
}

function About() {
  return <h2>About</h2>;
}

function Contact() {
  return <h2>Contact</h2>;
}

function App() {
  return (
    <BrowserRouter>

      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>

    </BrowserRouter>
  );
}

export default App;


## Syntax Explanation

BrowserRouter
- enables routing system

Link to="/about"
- navigates without reload

Routes
- holds all routes

Route path="/about"
- URL path

element={<About />}
- component to render

## Flow

Click Link → URL changes → matching Route → component renders

------------------------------------
SET 4 – Q1: LIKE BUTTON (TOGGLE)
------------------------------------

## Code

import { useState } from "react";

function Like() {
  const [liked, setLiked] = useState(false);

  return (
    <button onClick={() => setLiked(!liked)}>
      {liked ? "❤️" : "🤍"}
    </button>
  );
}

export default Like;


## Syntax Explanation

useState(false)
- initial state = not liked

liked
- current state (true/false)

setLiked(!liked)
- toggles value

? :
- conditional rendering

## Flow

Click → state flips → UI updates → heart changes

------------------------------------
SET 4 – Q2: FETCH API (NAME + WEBSITE)
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
          <p>{user.name}</p>
          <p>{user.website}</p>
        </div>
      ))}
    </div>
  );
}

export default Users;


## Syntax Explanation

useState([])
- stores list

useEffect(() => {}, [])
- runs once

fetch(url)
- API call

.then(res => res.json())
- convert to JSON

setUsers(data)
- store data

users.map()
- loop through users

key={user.id}
- unique identifier

## Flow

Component loads → fetch API → store → map → display

------------------------------------
FINAL QUICK SUMMARY
------------------------------------

Form → input + state  
Routing → page navigation  
Toggle → boolean flip  
Fetch → API + map display
