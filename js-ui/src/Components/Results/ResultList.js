import React from 'react'
import "./ResultList.css"


function ResultList(props){
    const DisplayData=props.keywords.map(
        (keyword)=>{
            return(
                <tr>
                    <td>{keyword}</td>
                </tr>
            )
        }
    )

    return(
        <div>
            <table className="table">
                <thead>
                    <tr>
                    <th>Keywords</th>
                    </tr>
                </thead>
                <tbody>
                    
                    
                    {DisplayData}
                    
                </tbody>
            </table>
                
        </div>
    )
}

export default ResultList;