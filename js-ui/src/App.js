import "./App.css";
import { useState } from "react";
import Disclaimer from "./Components/Disclaimer/Disclaimer";
import ResultTable from "./Components/Results/ResultTable";
import ResultList from "./Components/Results/ResultList"
import { AutoComplete } from "./Components/Autocomplete/Autocomplete";

function App() {
  const [showDetails, setShowDetails] = useState(false);
  const [resultOutput, setResultOutput] = useState("");

  function getProsCons(output) {
    if(output !== ""){
      setResultOutput(output);
      setShowDetails(true);
    }
    else {
      setResultOutput(null);
      setShowDetails(false);
    }
  }
  
  return (
    <div className="App">
      <Disclaimer />
      <AutoComplete onGetProsCons={getProsCons}/>
      {showDetails && <ResultTable myJson={resultOutput}/>}
    </div>
  );
}


export default App;
