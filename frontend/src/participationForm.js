import Header from "./Header";
import React, { useState, useEffect } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";

function withRouter(Component) {
  function ComponentWithRouterProp(props) {
    let location = useLocation();
    let navigate = useNavigate();
    let params = useParams();
    return <Component {...props} router={{ location, navigate, params }} />;
  }

  return ComponentWithRouterProp;
}

function ParticipationForm(props) {
  const [participant, setParticipant] = useState([]);
  const [email, setEmail] = useState([]);
  const [name, setName] = useState([]);
  const [surname, setSurname] = useState([]);
  const [password, setPassword] = useState([]);

  const addParticipant = () => {
    setParticipant([
      ...participant,
      {
        email: email,
        name: name,
        surname: surname,
        password: password,
      },
    ]);
  };

  async function addCourse() {
    let result = await fetch("http://localhost:8080/participations", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        training_id: props.router.params.id,
        users_to_register: participant,
      }),
    });
  }

  return (
    <div>
      <Header />
      <div>
        <button onClick={addParticipant} className={"button"}>
          <span>Add participant</span>
        </button>
        <input
          type="text"
          value={email}
          onChange={(e) => {
            setEmail(e.target.value);
          }}
          placeholder="Email"
        />
        <input
          type="text"
          value={name}
          onChange={(e) => {
            setName(e.target.value);
          }}
          placeholder="Name"
        />
        <input
          type="text"
          value={surname}
          onChange={(e) => {
            setSurname(e.target.value);
          }}
          placeholder="Surname"
        />
        <input
          type="password"
          value={password}
          onChange={(e) => {
            setPassword(e.target.value);
          }}
          placeholder="Password"
        />

        {participant.map((item) => (
          <ul>
            <li>
              Name: {item.name} Surname: {item.surname} Email: {item.email}
            </li>
          </ul>
        ))}
        <button onClick={addCourse} className={"button"}>
          <span>Add to course</span>
        </button>
      </div>
    </div>
  );
}

export default withRouter(ParticipationForm);
