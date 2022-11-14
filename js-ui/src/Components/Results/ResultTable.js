import { JsonToTable } from "react-json-to-table";

import "./ResultTable.css"

function ResultTable(props) {
    const newJson = {
        'Keywords': props.myJson.keywords
    }

    return(
        <div className="resultTable">
            <JsonToTable json={newJson}/>
        </div>
    )
}

export default ResultTable