# Web Development II — Exam Notes (Organized Answers)

Author: Generated exam-oriented answers
Date: 2026-05-23

---

**How to use:** These notes are organized by sections and questions. Each short answer is 2 marks (4–6 lines). Long answers are detailed for 8-mark style and include examples and code.

**Tags used:** (2 Marks), (5 Marks), (8 Marks), **Very Important** where noted.

## SECTION A — SHORT ANSWER QUESTIONS (2 MARKS)

1. **Define the DOM and explain its role in web development.**  
- **Marks / Importance:** (2 Marks) — **Very Important**  
- **Answer:**  
	- **DOM (Document Object Model)** is a tree-like object representation of an HTML or XML document where each node represents elements, text, and attributes.  
	- It exposes a programmatic API (e.g., `document`, element methods) enabling JavaScript to read and modify page structure, content, and styles dynamically.  
	- Browsers construct the DOM from HTML; changes to the DOM update the rendered page.  
	- Practical uses include updating text, inserting elements, and handling user events without reloading the page.

2. **Explain DOM vs HTML.**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- **HTML** is the static markup source file that the developer writes.  
	- **DOM** is the browser’s live in-memory object model built from that HTML and accessible via JavaScript.  
	- HTML is plain text; DOM is a manipulable structure (use `createElement`, `appendChild`).  
	- Updating the DOM changes the live UI; editing the HTML file affects future loads.

3. **Difference between textContent, innerHTML, and innerText.**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- **`textContent`** returns/sets raw text including hidden text and is safe (no HTML parsing).  
	- **`innerText`** returns the rendered visible text (CSS-aware) and may be slower.  
	- **`innerHTML`** returns/sets HTML markup inside an element (can inject elements and scripts — security risk if untrusted).  
	- Use `textContent` for plain text, `innerHTML` for markup injection, `innerText` for visible text reading.

4. **Difference between getElementById(), getElementsByClassName(), querySelector(), and querySelectorAll().**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- **`getElementById(id)`**: returns single element or `null`, fastest, selects by id.  
	- **`getElementsByClassName(className)`**: returns a live `HTMLCollection` of matching elements.  
	- **`querySelector(selector)`**: returns the first match for a CSS selector (static at call time).  
	- **`querySelectorAll(selector)`**: returns a static `NodeList` of all matches; supports complex selectors.

5. **What are classList methods (add/remove/toggle)?**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- `element.classList.add('c')` adds a class if not present.  
	- `element.classList.remove('c')` removes a class if present.  
	- `element.classList.toggle('c', force?)` toggles the class; with boolean forces add/remove.  
	- `classList` also provides `contains()` and `replace()`; it is safer than manipulating `className` strings.

6. **Discuss microtask and macrotask queue.**  
- **Marks / Importance:** (2 Marks) — **Very Important**  
- **Answer:**  
	- **Macrotasks (task queue):** callbacks from `setTimeout`, `setInterval`, I/O, and UI events — scheduled per event loop turn.  
	- **Microtasks (microtask queue):** Promise `.then/.catch/.finally` and `queueMicrotask` — run immediately after the current script finishes and before the next macrotask.  
	- Microtasks have higher priority, so they run before macrotasks; this ordering explains subtleties in async output ordering.  
	- Understanding both is essential for predictable async behavior.

7. **Difference between setTimeout() and setInterval().**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- `setTimeout(fn, ms)` runs `fn` once after at least `ms` milliseconds.  
	- `setInterval(fn, ms)` runs `fn` repeatedly every `ms` milliseconds until cleared.  
	- Use `setTimeout` for single delayed actions; prefer recursive `setTimeout` for variable intervals and avoiding overlaps.  
	- Clear with `clearTimeout(id)` or `clearInterval(id)`.

8. **What is Callback Hell? Explain its disadvantages.**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- **Callback Hell** (pyramid of doom) is deeply nested callbacks when async tasks depend on previous ones.  
	- Disadvantages: hard-to-read code, difficult error handling, and poor maintainability.  
	- It increases risk of duplicated logic and bugs; Promises/async-await address these issues by flattening flow.  
	- Use Promises or `async/await` to write clearer async sequences.

9. **What are Promise states in JavaScript?**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- **Pending:** initial unresolved state.  
	- **Fulfilled (Resolved):** operation succeeded and value available.  
	- **Rejected:** operation failed and reason available.  
	- Once settled (fulfilled or rejected) the state is immutable; use `.then()`, `.catch()`, `.finally()` to consume results.

10. **Explain the Event Loop and how asynchronous code executes in JavaScript.**  
- **Marks / Importance:** (2 Marks) — **Very Important**  
- **Answer:**  
	- JavaScript runs on a single thread with a **call stack**.  
	- When async APIs are used, callbacks are registered and moved to **microtask** or **macrotask** queues after the current stack clears.  
	- The **event loop** processes all microtasks first, then one macrotask, then renders, and repeats.  
	- This model allows non-blocking I/O while preserving single-threaded execution semantics.

11. **What is JSX in React?**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- **JSX** is a JavaScript syntax extension that resembles HTML used in React to declare UI.  
	- Babel transpiles JSX into `React.createElement()` calls.  
	- JSX supports embedding JS expressions with `{}` and improves readability of component markup.  
	- It is optional but common for writing React components.

12. **What is one-way data binding?**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- **One-way data binding** means data flows from parent (state) → child (props) only.  
	- Children cannot change parent state directly; they must call handler props passed from parent.  
	- This makes data flow predictable and easier to debug.  
	- For two-way behavior, pass callbacks to update parent state.

13. **What are Hooks? State the rules of Hooks.**  
- **Marks / Importance:** (2 Marks) — **Very Important**  
- **Answer:**  
	- **Hooks** are functions such as `useState`, `useEffect` that let functional components use state and lifecycle features.  
	- **Rules of Hooks:** (1) Only call hooks at the top level of React function components or custom hooks. (2) Only call hooks from React functions (not regular JS functions).  
	- Hooks must be called in the same order each render; they replace many class patterns for simpler code.

14. **Demonstrate the role of useState using a simple example.**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- `useState` creates state in functional components: `const [count, setCount] = useState(0);`  
	- `setCount(newValue)` schedules state update and triggers re-render.  
	- Example:  
	```jsx
	function Counter(){
		const [count, setCount] = useState(0);
		return <button onClick={()=>setCount(count+1)}>{count}</button>;
	}
	```
	- `useState` keeps UI in sync across renders.

15. **Define props in React with a simple use case.**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- **Props** are read-only inputs passed from parent to child components.  
	- Use case: `<Greeting name="Ali" />` and in child: `function Greeting({name}) { return <h1>Hello {name}</h1>; }`  
	- Props enable component reuse and customization without internal mutation.

16. **Differentiate between Local Storage and Session Storage.**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- **LocalStorage:** persistent across browser sessions until removed; stores strings per origin.  
	- **SessionStorage:** lasts for the tab session and clears when tab/window closes.  
	- Both are synchronous and limited in size; use `JSON.stringify`/`parse` for objects.  
	- Use localStorage for long-term preferences, sessionStorage for short-lived data.

17. **Explain the role of Babel in converting modern JavaScript code.**  
- **Marks / Importance:** (2 Marks) — **Very Important**  
- **Answer:**  
	- **Babel** is a compiler that transpiles modern JavaScript (ES6+, JSX) into browser-compatible code.  
	- It enables features like arrow functions, classes, optional chaining while targeting older environments.  
	- Babel uses plugins/presets and can include polyfills (with `core-js`).  
	- In React, Babel converts JSX into `createElement` calls.

18. **How does React manage frequent UI updates efficiently?**  
- **Marks / Importance:** (2 Marks) — **Very Important**  
- **Answer:**  
	- React uses a **Virtual DOM** (in-memory tree) to compute diffs and apply minimal DOM updates.  
	- Reconciliation batches updates and React optimizes re-renders via keys, `React.memo`, and hooks like `useMemo`.  
	- Minimizing direct DOM operations improves performance for frequent updates.

19. **Explain the use of dependency array in useEffect.**  
- **Marks / Importance:** (2 Marks) — **Very Important**  
- **Answer:**  
	- `useEffect(fn, [dep1, dep2])` runs the effect when any dependency changes.  
	- `[]` runs once on mount; omitting the array runs after every render.  
	- Proper dependencies avoid stale closures and unnecessary effect calls.  
	- Use `useCallback`/`useMemo` to stabilize functions/objects in the array.

20. **Disadvantage of props drilling.**  
- **Marks / Importance:** (2 Marks)  
- **Answer:**  
	- **Props drilling** forces passing props through intermediate components that don't use them, cluttering APIs and hurting maintainability.  
	- It increases coupling and makes refactoring harder; many components must update when prop shapes change.  
	- Context API or state management libraries (Redux) solve this by providing direct access to nested consumers.

---

## SECTION B — LONG ANSWER QUESTIONS (8 MARKS)

### Q1. Discuss event handling in JavaScript using addEventListener() with different event types.  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer:**  
	**Overview:** Event handling connects user/system actions (click, input, load) with JavaScript functions. Use `addEventListener()` to attach listeners.  
	**Syntax:** `element.addEventListener(type, listener, options)` where `options` may include `{capture, once, passive}`.  
	**Common options:**  
	- `capture`: run during capturing phase if true.  
	- `once`: auto-removes listener after first invocation.  
	- `passive`: indicates listener won't call `preventDefault()` — improves scrolling performance.  
	**Event types and examples:**  
	- **Mouse:** `click`, `dblclick`, `mousemove` — `btn.addEventListener('click', handler)`  
	- **Keyboard:** `keydown`, `keyup` — attach to window or inputs for key handling.  
	- **Form:** `submit`, `input`, `change` — use `preventDefault()` to control form submit.  
	- **Window:** `load`, `resize`, `scroll` — often use `passive: true` for performance.  
	**Best practices:**  
	- Prefer `addEventListener` vs inline handlers to allow multiple listeners.  
	- Use `once` to auto-clean listeners; call `removeEventListener` when needed.  
	- Keep listeners lightweight; debounce/throttle expensive handlers.  
	**Code example:**  
	```html
	<button id="btn">Click me</button>
	<script>
	const btn = document.getElementById('btn');
	function handler(e){ console.log('clicked', e.type); }
	btn.addEventListener('click', handler, {once:true});
	</script>
	```

### Q2. Explain event propagation. Differentiate between bubbling and capturing. Also discuss the role of event listeners.  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer:**  
	**Definition:** Event propagation determines how events travel through the DOM tree. Phases: capturing → target → bubbling.  
	**Capturing (downward):** event moves from document root down to the target; listeners with `{capture:true}` run here.  
	**Target:** the event reaches the target element — target listeners execute.  
	**Bubbling (upward):** event bubbles from target up to root; default listeners (no capture) run here.  
	**Control methods:**  
	- `stopPropagation()` prevents further propagation.  
	- `stopImmediatePropagation()` prevents other listeners on the same element.  
	- `preventDefault()` prevents default browser behavior (does not stop propagation).  
	**Use cases:**  
	- **Event delegation:** attach a single listener on ancestor and use bubbling to handle many children efficiently.  
	- **Capturing:** intercept events before children (rare but useful for certain patterns).  
	**Example:**  
	```js
	parent.addEventListener('click', ()=>console.log('parent bubble'));
	parent.addEventListener('click', ()=>console.log('parent capture'), {capture:true});
	```

### Q3. Simple webpage demonstrating button click events and event removal  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer (HTML + CSS + JS):**  
```html
<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Button Click & removeEventListener Demo</title>
	<style>body{font-family:Arial;padding:20px}#message{font-size:20px;color:#333}#changeBtn{padding:8px 12px}</style>
</head>
<body>
	<h2 id="message">This is the default message.</h2>
	<button id="changeBtn">Click me once</button>
	<script>
		const message = document.getElementById('message');
		const btn = document.getElementById('changeBtn');
		function handleClick(){
			message.textContent = 'Message updated! Button will no longer work.';
			message.style.color = 'crimson';
			btn.removeEventListener('click', handleClick);
			btn.disabled = true; btn.textContent = 'Done';
		}
		btn.addEventListener('click', handleClick);
	</script>
</body>
</html>
```

**Notes:** `removeEventListener` requires the same function reference. Alternatively use `{once:true}` when adding listener.

### Q4. Explain execution context in JavaScript including GEC, FEC, and Call Stack.  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer:**  
	**Execution context** is an abstract environment where JS code is evaluated: it contains variable/environment records and `this` value.  
	**Global Execution Context (GEC):** created at program start; attaches global object (`window`) and global scope.  
	**Functional Execution Context (FEC):** created on each function call; has its own variable object, arguments, scope chain, and `this`.  
	**Creation vs Execution phases:** creation hoists declarations; execution runs code line-by-line.  
	**Call Stack:** stack of active execution contexts; GEC pushed first; each function call pushes a new FEC; returns pop the stack.  
	**Example:**  
	```js
	function a(){ b(); console.log('a done'); }
	function b(){ console.log('in b'); }
	a();
	// call stack: GEC -> a -> b; b returns, a returns, then back to GEC
	```

### Q5. Explain the lifecycle of a Promise  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer:**  
	**Problem of Callback Hell:** Nested callbacks are hard to read and manage. Promises provide clearer, chainable async control.  
	**Definition:** A **Promise** represents an async operation that will eventually produce a value (fulfill) or reason for failure (reject).  
	**States:** `Pending` → `Fulfilled` or `Rejected` (settled and immutable).  
	**Consumers:** `.then(onFulfilled, onRejected)`, `.catch(onRejected)`, `.finally(onFinally)`.  
	**Example:**  
	```js
	function fetchData(url){
		return new Promise((resolve,reject)=>{
			fetch(url)
				.then(res => res.ok ? res.json() : Promise.reject('Network error'))
				.then(data => resolve(data))
				.catch(err => reject(err));
		});
	}
	fetchData('/api').then(data=>console.log(data)).catch(e=>console.error(e));
	```
	**Chaining & composition:** Promises allow `.then()` chains and helpers like `Promise.all`, `Promise.race` for composition.

### Q6. Explain async/await with error handling using try...catch.  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer:**  
	**Overview:** `async/await` builds on Promises to write asynchronous code in synchronous style. `async` marks a function and `await` pauses until a promise settles.  
	**Error handling:** Use `try { await ... } catch (err) { ... } finally { ... }` to handle rejections and cleanup.  
	**Example:**  
	```js
	async function fetchUser(){
		try{
			const res = await fetch('https://jsonplaceholder.typicode.com/users/1');
			if(!res.ok) throw new Error('Network error');
			const user = await res.json();
			return user;
		}catch(err){ console.error(err); throw err; }
		finally{ console.log('done'); }
	}
	```
	**Best practices:** Avoid unnecessary sequential awaits when tasks are independent; prefer `Promise.all` for concurrency.

### Q7. React: Fetch API data from https://jsonplaceholder.typicode.com/users  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer — Code:**  
```jsx
import React, {useState, useEffect} from 'react';

function UsersList(){
	const [users, setUsers] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	useEffect(()=>{
		let mounted = true;
		fetch('https://jsonplaceholder.typicode.com/users')
			.then(res => { if(!res.ok) throw new Error('Network'); return res.json(); })
			.then(data => { if(mounted) setUsers(data); })
			.catch(err => { if(mounted) setError(err.message)})
			.finally(()=> { if(mounted) setLoading(false)});
		return ()=> { mounted = false; };
	}, []);

	if(loading) return <p>Loading users...</p>;
	if(error) return <p>Error: {error}</p>;

	return (
		<div>
			<h2>Users</h2>
			<ul>
				{users.map(u => (
					<li key={u.id}><strong>{u.username}</strong> — {u.email}</li>
				))}
			</ul>
		</div>
	);
}
export default UsersList;
```

### Q8. Explain component lifecycle methods in React and how they are implemented using useEffect with examples.  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer:**  
	**Class lifecycle methods:** `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`, `componentDidCatch`.  
	**Hooks (useEffect) equivalents:**  
	- **Mount only:** `useEffect(()=>{ /*did mount*/ }, [])`  
	- **Update:** `useEffect(()=>{ /*did update*/ }, [dep])`  
	- **Unmount cleanup:** `useEffect(()=>{ return ()=>{/*cleanup*/}; }, [])`  
	**Examples:**  
	```jsx
	useEffect(()=>{ console.log('mounted'); }, []);
	useEffect(()=>{ console.log('count changed', count); }, [count]);
	useEffect(()=>{ const id=setInterval(()=>{},1000); return ()=>clearInterval(id); }, []);
	```
	**Notes:** Effects run after paint and do not block render; use multiple effects to separate concerns.

### Q9. React: Two buttons, one popup every click, second updates counter without popup  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer — Code:**  
```jsx
import React, {useState, useEffect} from 'react';

function CounterWithPopup(){
	const [count, setCount] = useState(0);
	const [showPopupFlag, setShowPopupFlag] = useState(false);

	useEffect(()=>{ if(!showPopupFlag) return; alert('Popup: Button clicked!'); setShowPopupFlag(false); }, [showPopupFlag]);

	return (
		<div>
			<h3>Counter: {count}</h3>
			<button onClick={()=>setShowPopupFlag(true)}>Show Popup</button>
			<button onClick={()=>setCount(prev=>prev+1)}>Increment (no popup)</button>
		</div>
	);
}
export default CounterWithPopup;
```

### Q10. User Information Form using React (Name, Age, Gender, Languages; show submitted data)  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer — Code (controlled form):**  
```jsx
import React, {useState} from 'react';

function UserForm(){
	const [form, setForm] = useState({name:'', age:'', gender:'', languages:{english:false,hindi:false,french:false}});
	const [submitted, setSubmitted] = useState(null);

	function handleChange(e){
		const {name, value, type, checked} = e.target;
		if(type==='checkbox'){
			setForm(prev=>({ ...prev, languages:{ ...prev.languages, [name]: checked }}));
		} else setForm(prev=>({ ...prev, [name]: value }));
	}

	function handleSubmit(e){ e.preventDefault(); const selected = Object.keys(form.languages).filter(k=>form.languages[k]); setSubmitted({...form, languages:selected}); }

	return (
		<div>
			<form onSubmit={handleSubmit}>
				<label>Name:<input name="name" value={form.name} onChange={handleChange} required /></label><br/>
				<label>Age:<input name="age" type="number" value={form.age} onChange={handleChange} required /></label><br/>
				<label>Gender:<select name="gender" value={form.gender} onChange={handleChange} required><option value="">Select</option><option value="male">Male</option><option value="female">Female</option><option value="other">Other</option></select></label>
				<fieldset><legend>Languages</legend>
					<label><input type="checkbox" name="english" checked={form.languages.english} onChange={handleChange}/> English</label>
					<label><input type="checkbox" name="hindi" checked={form.languages.hindi} onChange={handleChange}/> Hindi</label>
					<label><input type="checkbox" name="french" checked={form.languages.french} onChange={handleChange}/> French</label>
				</fieldset>
				<button type="submit">Submit</button>
			</form>
			{submitted && (<div><h4>Submitted Data</h4><p><strong>Name:</strong> {submitted.name}</p><p><strong>Age:</strong> {submitted.age}</p><p><strong>Gender:</strong> {submitted.gender}</p><p><strong>Languages:</strong> {submitted.languages.join(', ') || 'None'}</p></div>)}
		</div>
	);
}
export default UserForm;
```

### Q11. Counter app: Increment, Decrement, Reset using useState  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer — Code:**  
```jsx
import React, {useState} from 'react';
function CounterApp(){ const [count, setCount] = useState(0); return (<div><h2>Counter: {count}</h2><button onClick={()=>setCount(c=>c+1)}>Increment</button><button onClick={()=>setCount(c=>c-1)}>Decrement</button><button onClick={()=>setCount(0)}>Reset</button></div>); }
export default CounterApp;
```

### Q12. Explain Context API and compare it with Props Drilling. Implement data sharing across nested components.  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer:**  
	**What is Context:** React Context provides a way to pass data through the component tree without passing props manually at every level.  
	**When to use:** global data like theme, auth, or locale.  
	**Comparison table:**
  
	| Aspect | Props Drilling | Context API |
	|---|---:|---|
	| Complexity | High (many prop forwards) | Low (direct consumer access)
	| Boilerplate | Many intermediate props | Provider + consumers
	| Coupling | Intermediate components depend on props | Intermediate unaffected

	**Example:**
	```jsx
	const UserContext = React.createContext(null);
	function App(){ const user = {name:'Aisha'}; return <UserContext.Provider value={user}><Level1/></UserContext.Provider>; }
	function Level1(){ return <Level2/>; }
	function Level2(){ return <Level3/>; }
	function Level3(){ const user = React.useContext(UserContext); return <p>{user.name}</p>; }
	```

### Q13. Discuss disadvantages of props drilling and explain how Context API solves them.  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer:**  
	**Disadvantages of props drilling:**  
	- Verbose and repetitive — many intermediate components must forward props.  
	- Tight coupling and harder refactor; any prop shape change affects many components.  
	- Increased chance of unnecessary re-renders in intermediate components.  
	**How Context helps:**  
	- Provides direct access to data for nested consumers without forwarding.  
	- Reduces boilerplate and decouples intermediate components from data.  
	**Caveat:** Overusing Context can hide dependencies; use multiple focused contexts to minimize re-renders.

### Q14. Explain routing in React with example and create multiple pages with navigation.  
- **Marks / Importance:** (8 Marks) — **Very Important**  
- **Answer:**  
	**Overview:** Routing enables multi-page feel in single-page apps. Use `react-router-dom` for declarative routes.  
	**Key parts:** `BrowserRouter`, `Routes`, `Route`, `Link`, `NavLink`, `useParams`, `useNavigate`.  
	**Example:**
	```jsx
	import {BrowserRouter, Routes, Route, Link} from 'react-router-dom';
	function App(){
		return (
			<BrowserRouter>
				<nav><Link to="/">Home</Link> | <Link to="/about">About</Link></nav>
				<Routes>
					<Route path="/" element={<Home/>} />
					<Route path="/about" element={<About/>} />
				</Routes>
			</BrowserRouter>
		);
	}
	```
	**Notes:** Use `NavLink` for active styles and configure server to serve `index.html` for client routes.

---

## EXTRA: Output-based question (Event Loop example)

**Code:**
```js
console.log("Start");
async function test(){
	console.log("Inside function");
	await Promise.resolve();
	console.log("After await");
}
test();
setTimeout(()=>{ console.log("Timeout"); }, 0);
console.log("End");
```

**Output (order):**
1. Start
2. Inside function
3. End
4. After await
5. Timeout

**Reason:** `await` defers the continuation as a microtask; microtasks run after current stack but before macrotasks (setTimeout). So the promise continuation logs before the timeout.

---

If you want this file split into separate topic files or exported as PDF/printable notes, I can create those next.

