import React ,{useState, useEffect} from 'react'
import Header from './Header'
import { useNavigate} from "react-router-dom";


function Login()
{


    const [email,setEmail]=useState("");
    const [password,setPassword]=useState("");
    const navigate = useNavigate();

               useEffect(()=>{
               if(localStorage.getItem("user-info")){
               navigate("/createCourseForWorker")
               }
               },[])





    async function login()
        {
        let item={email, password}


        let result= await fetch("http://localhost:8080/auth/login",{
        method:"POST",
        body: new URLSearchParams({
                email: email,
                password: password
        })
            })
            result = await result.json()
            localStorage.setItem("user-info", JSON.stringify(result))
            navigate("/createCourseForWorker")


        }

return (
            <div>
            <Header/>
            <div className="col-sm-4 offset-sm-4">
                        <h1> Login page </h1>
                        <input type="text" value={email} onChange={(e)=>setEmail(e.target.value)} className="form-control" placeholder="email"/>
                        <br />
                        <input type="password" value={password} onChange={(e)=>setPassword(e.target.value)} className="form-control" placeholder="password"/>
                        <br />
                        <button onClick={login} className="btn btn-primary"> Login </button>
            </div>
            </div>
)
}

export default Login