import { useState } from 'react';
import './App.css';
import PendingCard from './components/PendingCard';
import PreparingCard from './components/PreparingCard'
function App() {

  const [pendingList, setPendingList] = useState([]);
  const [preparingList, setPreparingList] = useState([]);

  return (
    <div className="App">
      <div id="navbar">
        <h1>EasyServe</h1>
      </div>
      <div class="container">
      <div id="pending">
      </div>
      <div id="preparing">
      </div>

      </div>
      
    </div>
  );
}

export default App;
