import { useEffect, useState } from "react";
// useState = store data
// useEffect = run API call

function Users() {
  const [users, setUsers] = useState([]); 
  // array to store users

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users") 
    // API call

      .then(res => res.json()) 
      // convert response to JSON

      .then(data => setUsers(data)); 
      // store data in state

  }, []); 
  // [] = run only once

  return (
    <div>
      {users.map(user => (
        <div key={user.id}> 
          {/* key helps React track list */}

          <p>{user.name}</p> 
          {/* display name */}

          <p>{user.website}</p> 
          {/* display website */}
        </div>
      ))}
    </div>
  );
}

export default Users;
