import React ,{useState} from 'react'

function Login()
{

    const [email,setEmail]=useState("")
    const [password,setPassword]=useState("")


    async function login()
        {
        let item={email, password}
        console.warn(item)

        let result= await fetch("http://localhost:8080/auth/login",{
        method:"POST",
        body: new URLSearchParams({
                email: email,
                password: password
        })
            })
            result = await result.json()
            console.warn("result", result)
        }

return (
            <div className="col-sm-4 offset-sm-4">
                        <h1> Login page </h1>
                        <input type="text" value={email} onChange={(e)=>setEmail(e.target.value)} className="form-control" placeholder="email"/>
                        <br />
                        <input type="password" value={password} onChange={(e)=>setPassword(e.target.value)} className="form-control" placeholder="password"/>
                        <br />
                        <button onClick={login} className="btn btn-primary"> Login </button>
            </div>
)
}

export default Login