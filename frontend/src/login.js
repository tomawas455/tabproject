import React, { useState, useEffect } from "react";
import Header from "./Header";
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    if (localStorage.getItem("user-info")) {
      navigate("/createCourseForWorker");
    }
  }, []);

  async function login() {
    let item = { email, password };

    let result = await fetch("http://localhost:8080/auth/login", {
      method: "POST",
      credentials: "include",
      body: new URLSearchParams({
        email: email,
        password: password,
      }),
    }).then((response) => {
      if (response.status >= 400 && response.status < 600) {
        alert("Wrong Login or Password !", "Title");
        throw new Error("Bad response from server");
      }
      return response;
    });
    result = await result.json();
    localStorage.setItem("user-info", JSON.stringify(result));
    console.log("login", result.headers);
    navigate("/createCourseForWorker");
  }

  return (
    <div>
      <Header />
      <div className="col-sm-4 offset-sm-4">
        <h1> Login page </h1>
        <input
          type="text"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="form-control"
          placeholder="email"
        />
        <br />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="form-control"
          placeholder="password"
        />
        <br />
        <button onClick={login} className="button">
          <span> Login </span>
        </button>
      </div>
    </div>
  );
}

export default Login;
