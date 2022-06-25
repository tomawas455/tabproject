import React, { useState } from "react";
import Header from "./Header";

function Register() {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [password, setPassword] = useState("");

  async function signUp() {
    let item = { email, name, surname, password };
    console.warn(item);

    let result = await fetch("http://localhost:8080/auth/register", {
      method: "POST",
      body: new URLSearchParams({
        email: email,
        name: name,
        surname: surname,
        password: password,
      }),
    });
    result = await result.json();
    console.warn("result", result);
  }

  return (
    <div>
      <Header />
      <div className="col-sm-4 offset-sm-4">
        <h1> Register Page </h1>
        <input
          type="text"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="form-control"
          placeholder="email"
        />
        <br />
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="form-control"
          placeholder="name"
        />
        <br />
        <input
          type="text"
          value={surname}
          onChange={(e) => setSurname(e.target.value)}
          className="form-control"
          placeholder="surname"
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
        <button onClick={signUp} className="btn btn-primary">
          {" "}
          Sign Up{" "}
        </button>
      </div>
    </div>
  );
}

export default Register;
