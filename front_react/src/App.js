import './App.css';
import {useState} from "react";
import React from "react";

function App() {
    const [auth, setAuth] = useState( false);
    const [login, setLogin] = useState( '');
    const [password, setPassword] = useState( '');

    function get_login() {
        let data ={
            "username":login,
            "password":password
        }
        fetch( 'http://127.0.0.1:8000/api/v1/super'), {
            method : "POST",
            body:JSON.stringify(data)
        }
            .then(response=>response.json())
            .then(p=>console.log(p))
        console.log(11111)
    }

    if(auth){
        return
        <div>
            <h1>hello your in account</h1>
        </div>
    }
    else {
        return (
            <div className="App">
                <form action="">
                    <input type="text" placeholder={'enter login'} onChange={(e)=>setLogin(e.target.value)}/><br/>
                    <input type="password" placeholder={'enter pass'} onChange={(e)=>setPassword(e.target.value)}/><br/>
                    <input type="button" onClick={get_login} value={'login'}/>
                </form>
            </div>
        );
    }

}

export default App;
