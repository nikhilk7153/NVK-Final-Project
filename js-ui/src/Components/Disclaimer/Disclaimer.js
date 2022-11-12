import './Disclaimer.css'

function Disclaimer() {
    return (
        <div className='disclaimer'>
            <h3>CS410 Project - NVK</h3>
            <h4>Kyr Nastahunin, Nikhil Khandekar, Vineet Chinthakindi</h4>
            <p>This webpage allows to find a a yelp business and discover the key points about the pros and cons of it's operation.<br></br>
                We used the following documents as our source: <br></br>
                <a href='https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents'>Automatic Keyword Extraction from Individual Documents</a>
                &nbsp;and&nbsp;
                <a href='https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf'>TextRank: Bringing Order into Texts</a>
            </p>
        </div>
    )
}

export default Disclaimer;