import './SearchBar.css'
import { useState } from 'react';
import axios from 'axios';

function SearchBar(props) {
    const [search, setSearch] = useState("")

    async function getProsCons(event) {
        event.preventDefault();
        const result = await axios.get("https://httpbin.org/get")
        console.log(search)
        props.onGetProsCons(result.data.data)
    }

    function formChangeHandler(event){
        setSearch(event.target.value)
    }

    return(
        <div>
            <form onSubmit={getProsCons}>
                <input type="text" onChange={formChangeHandler}/>
                <button type="submit">Search</button>
            </form>
        </div>
    )
}

export default SearchBar;