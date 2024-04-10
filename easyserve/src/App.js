import { useState } from 'react';
import './App.css';
import PendingCard from './components/PendingCard';
import PreparingCard from './components/PreparingCard'
function App() {

  const [pendingList, setPendingList] = useState([]);
  const [preparingList, setPreparingList] = useState([]);

  function handlePending(item){
    let temp = preparingList;
    temp.push(item);
    setPreparingList(temp);
  }
  function handlePreparing(id){
    
  }
  return (
    <div className="App">
      <div id="navbar">
        <h1>EasyServe</h1>
      </div>
      <div class="container">
      <div id="pending">
      {pendingList.map((instance)=>{
                return(
                    <PendingCard onFinished={handlePending} item={instance.items}/>
                )
            })}
      </div>
      <div id="preparing">
      {preparingList.map((instance)=>{
                return(
                    <PreparingCard onFinished={handlePreparing} item={instance.items}/>
                )
            })}
      </div>

      </div>
      
    </div>
  );
}

export default App;
