import './App.css';
import {useState,useEffect} from "react";

function App() {

    const [category, setCategory] = useState([{"name": 'нажми кнопку категории'}])
    const [services, setServices] = useState([{"title": 'нажми кнопку сервисы'}])

    useEffect(()=>{
        fetch('http://127.0.0.1:8000/api/v1/categoryes/')
            .then(response=>response.json())
            .then(data=>{
                setCategory(data)
            })
    },[])
    useEffect(()=>{
        fetch('http://127.0.0.1:8000/api/v1/services/')
            .then(response=>response.json())
            .then(data=>{
                setServices(data)
            })
    },[])
    console.log(category)
    return (
        <>
            <div className="App">
                <h1>Hello MAD Max</h1>
            </div>
            <nav >
                <ul style={{display:"flex",width:'80%',justifyContent:"flex-start",background:"blue"}}>
                    {category.map(item=><li style={{margin:"15px",color:"yellow"}} key={item.name}>{item.name}</li>)}
                </ul>

            </nav>
            <h3>Сервисы</h3>
            <main style={{
                display:"flex",
                width:'80%',
                justifyContent:"flex-start",
                background:"grey",
                padding:'20px'}}>
                {services.map(item=><div style={{
                    height:'150px',
                    width:'150px',
                    border:"1px solid red",
                    background:"goldenrod",
                    margin:"20px"}} key={item.title}><p>{item.title}</p><p>{item.price}</p></div>)}

            </main>
        </>
    );
}

export default App;