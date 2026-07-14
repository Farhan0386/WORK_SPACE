import { useState } from "react"; // hook to store changing data

function Form() {
  const [name, setName] = useState(""); 
  // name = current value
  // setName = function to update value
  // "" = initial empty input

  return (
    <div>
      <input
        type="text"
        placeholder="Enter name"
        onChange={(e) => setName(e.target.value)} 
        // onChange = runs when user types
        // e.target.value = current input text
        // setName updates state
      />

      <h2>{name}</h2> 
      {/* displays updated value in real-time */}
    </div>
  );
}

export default Form;