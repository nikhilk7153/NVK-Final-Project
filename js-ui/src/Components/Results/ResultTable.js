import { JsonToTable } from "react-json-to-table";

function ResultTable(props) {
    const newJson = {
        'Pros': props.myJson.pros,
        'Cons': props.myJson.cons
    }

    return(
        <div className="detailsTable">
            <JsonToTable json={newJson}/>
        </div>
    )
}

export default ResultTable