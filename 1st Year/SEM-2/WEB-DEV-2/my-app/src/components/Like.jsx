import { useState } from "react"; // for toggle state

function Like() {
  const [liked, setLiked] = useState(false); 
  // false = not liked initially

  return (
    <button onClick={() => setLiked(!liked)}>
      {/* !liked flips value: true ↔ false */}

      {liked ? "❤️" : "🤍"} 
      {/* if true → red heart, else white */}
    </button>
  );
}

export default Like;