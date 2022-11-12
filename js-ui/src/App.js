import './App.css';
import { useState } from 'react'
import Disclaimer from './Components/Disclaimer/Disclaimer';
import SearchBar from './Components/SearchBar/SearchBar';
import ResultTable from './Components/Results/ResultTable';

function App() {
  const [showDetails, setShowDetails] = useState(false)
  const [resultOutput, setResultOutput] = useState('')

  function getProsCons(output){
    const jsonOutput = JSON.parse(output)
    setResultOutput(jsonOutput)
    setShowDetails(true)
  }

  if (!showDetails){
    return (
      <div className="App">
        <Disclaimer />
        <SearchBar onGetProsCons={getProsCons}/>
      </div>
    );
  }
  else {
    return (
      <div className="App">
        <Disclaimer />
        <SearchBar onGetProsCons={getProsCons}/>
        <ResultTable myJson={resultOutput} />
      </div>
    );
  }
}

export default App;
