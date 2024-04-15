import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [Pokemon, setPokemon] = useState([]);

  const AxiosPokemon = () => {
    axios
      .get("https://pokeapi.co/api/v2/pokemon")
      .then((res) => {
        console.log(res);
        setPokemon(res.data.results);
        console.log(Pokemon);
      })
      .catch((err) => {
        console.log("❌❌❌❌❌❌", err);
      });
  };

  return (
    <div>
      <h1>Pokemon Fetcher</h1>
      <button onClick={AxiosPokemon}>fetch Pokemon</button>
      <ul>
        {Pokemon.map((pok) => (
          <li> {pok.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
