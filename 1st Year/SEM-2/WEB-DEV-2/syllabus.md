# UNIT 1

## DOM
- DOM = Document Object Model
- Represents HTML as tree structure
- JS can manipulate HTML using DOM

## DOM vs HTML
- HTML = static structure
- DOM = dynamic (can change using JS)

## Element Selection
# Web Development — Syllabus (Enhanced)

## Table of Contents
- [Course overview](#course-overview)
- [Learning outcomes](#learning-outcomes)
- [Unit 1: DOM & Events](#unit-1-dom--events)
- [Unit 2: Asynchronous JavaScript](#unit-2-asynchronous-javascript)
- [React Fundamentals](#react-fundamentals)
- [Practicals & Labs](#practicals--labs)
- [Assessment & Grading](#assessment--grading)
- [Important Questions / Exam Topics](#important-questions--exam-topics)
- [Resources & References](#resources--references)


## Course overview
This short syllabus covers core DOM concepts, asynchronous JavaScript, and essential React topics you need for practical web development. It includes learning outcomes, hands-on labs, assessment guidelines, and revision questions.


## Learning outcomes
By the end of this course students will be able to:
- Manipulate the DOM to update web pages dynamically.
- Understand event propagation and handle browser events correctly.
- Explain JavaScript's concurrency model (event loop, tasks, microtasks).
- Use Promises, async/await and the Fetch API for network calls.
- Build React components using `useState`, `useEffect`, and Context API.
- Create small single-page apps with routing and form handling.


## Unit 1: DOM & Events
Topics:
- Document Object Model (DOM): structure, nodes, tree representation.
- DOM vs HTML: static vs dynamic representation.
- Element selection methods: `getElementById`, `getElementsByClassName`, `querySelector`, `querySelectorAll`.
- Working with attributes, textContent, innerHTML, and value.
- `classList` methods: `add()`, `remove()`, `toggle()`, `contains()`.
- Event handling: `addEventListener`, event object, common events (`click`, `input`, `submit`).
- Event propagation: capturing vs bubbling; `stopPropagation()` and `preventDefault()`.
- Execution context basics: creation phase, execution phase, scope, hoisting (overview).

Practical exercises:
- Build a DOM inspector: select elements and display their attributes.
- Create a small interactive form that validates input and shows/hides messages.


## Unit 2: Asynchronous JavaScript
Topics:
- Synchronous vs asynchronous execution.
- Timers: `setTimeout`, `setInterval`, and clearing timers.
- Event loop: call stack, Web APIs, callback queue, and how the event loop schedules tasks.
- Microtasks vs macrotasks: Promises (`.then`) and `setTimeout` differences.
- Promises: creation, chaining, error handling with `.catch()`.
- `async` / `await` syntax and proper error handling with `try/catch`.
- Fetch API and basic HTTP methods (`GET`, `POST`), handling JSON responses.

Code example (fetch):
```js
fetch(url)
	.then(res => res.json())
	.then(data => console.log(data))
	.catch(err => console.error(err));
```

Practical exercises:
- Implement a client that fetches and displays a list of users from a public API.
- Compare behaviors of `setTimeout` and a resolved Promise in ordering logs.


## React Fundamentals
Topics:
- What is React? Component-based UI and Virtual DOM.
- JSX syntax and best practices.
- Functional components and hooks.
- `useState` for local component state.
- `useEffect` for side effects (data fetching, subscriptions, cleanup).
- Props: passing data from parent to child and prop validation principles.
- Context API: `createContext`, `Provider`, and `useContext` to avoid prop drilling.
- Routing basics: client-side routing concepts (e.g., `react-router` overview).
- Forms in React: controlled vs uncontrolled components and form submission.
- Component lifecycle approximated via hooks: mount, update, unmount.
- Styling: external CSS, inline styles, CSS modules.

Small component example:
```jsx
function App() {
	const [count, setCount] = useState(0);
	useEffect(() => {
		document.title = `Count: ${count}`;
	}, [count]);
	return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```


## Practicals & Labs
Core practicals to complete (suggested order):
1. Counter component — increment, decrement, reset (state + handlers).
2. Fetch and display data — use `useEffect` and handle loading/error states.
3. Controlled form — inputs, validation, and submission handling.
4. Simple multi-page SPA — implement routing for Home / About / Contact.
5. Context example — theme or auth state shared across components.

Assessment checkpoints:
- Lab submissions (code + short report).
- Mini-project: combine fetching, forms, and routing into a small app.


## Assessment & Grading
- Labs / Practicals: 40%
- Mini-project: 30%
- Quizzes & assignments: 20%
- Attendance & participation: 10%

Grading notes:
- Projects should be delivered with a README explaining setup and features.
- Code quality, readability, and use of React best practices are considered.


## Important Questions / Exam Topics
Focus areas for exams and long-answer questions:
- Event Loop and JavaScript concurrency (8 marks)
- Fetch API and request lifecycle (8 marks)
- `useState` and `useEffect` differences and examples (8 marks)
- Context API: when and how to use it (8 marks)
- Component lifecycle and cleanup in `useEffect` (8 marks)

Short questions (2 marks each):
- What is Babel? Why is it used?
- What is Webpack (or bundler) purpose?
- Explain Virtual DOM in one sentence.
- Props vs State — concise difference.


## Resources & References
- MDN Web Docs — JavaScript and DOM guides: https://developer.mozilla.org/
- React documentation: https://reactjs.org/
- Free APIs for practice: JSONPlaceholder, ReqRes
- Suggested reading: "You Don't Know JS (book series)" for deeper JS concepts.


---
If you want, I can also:
- add inline links to specific code examples in the repo,
- split the practicals into weekly schedule, or
- generate lab starter templates under `my-app/src/components`.
