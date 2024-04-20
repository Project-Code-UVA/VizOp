import React, {useState} from 'react';
import SampleGraph from './components/SampleGraph';
import LeftSidebar from './components/LeftSidebar';
import RightSidebar from './components/RightSidebar';
import './App.css';

function App() {

  const [graphData, setGraphData] = useState({}); 
  return (
    <div className="App-container" class = "bg-light">
      <header className='App-header' class = "bg-light" >
        <h1 className='project-name' class = "display-6" style={{ color: 'navy' }}>Viz<span style={{ color: 'orange' }}>Op</span></h1>
      </header>

      <body className='App-body'>
        <LeftSidebar setGraphData={setGraphData}/>
        <SampleGraph graphData={graphData}/>
        <RightSidebar />
      </body>
    </div>
  );
}

export default App;