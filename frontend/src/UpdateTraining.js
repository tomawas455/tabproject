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

function UpdateTraining(props) {
  const [userData, setUserData] = useState([]);
  const [data, setData] = useState([]);
  const [trainigData, setTrainingData] = useState([]);
  const [price, setPrice] = useState([]);
  const [placesAmount, setPlacesAmount] = useState([]);
  const [beginDate, setBeginDate] = useState([]);
  const [endDate, setEndDate] = useState([]);
  const [enrolmentBeginDate, setEnrolmentBeginDate] = useState([]);
  const [enrolmentEndDate, setEnrolmentEndDate] = useState([]);
  const [place, setPlace] = useState([]);
  const [instructor, setInstructor] = useState([]);

  useEffect(() => {
    cities();
    getUserData();
    getData();
  }, []);

  async function getData() {
    let result = await fetch(
      "http://localhost:8080/trainings/" + props.router.params.id,
      {
        credentials: "include",
        method: "GET",
      }
    );
    result = await result.json();
    setTrainingData(result);
  }

  async function cities() {
    let result = await fetch("http://localhost:8080/places", {
      credentials: "include",
      method: "GET",
    });
    result = await result.json();
    setData(result);
  }

  async function updateTrainingFunc() {
    await fetch("http://localhost:8080/trainings/7", {
      method: "PATCH",
      credentials: "include",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        Accept: "application/json",
      },
      body: new URLSearchParams({
        price: price,
        places_amount: placesAmount,
        begin_date: beginDate,
        end_date: endDate,
        enrolment_begin_date: enrolmentBeginDate,
        enrolment_end_date: enrolmentEndDate,
        place_id: place,
        instructor_id: instructor,
      }),
    });
    console.warn("training updated?");
    console.warn(price);
    console.warn(placesAmount);
    console.warn(beginDate);
    console.warn(endDate);
    console.warn(enrolmentBeginDate);
    console.warn(enrolmentEndDate);
    console.warn(place);
    console.warn(instructor);
  }

  async function getUserData() {
    let result = await fetch("http://localhost:8080/users/role/2", {
      credentials: "include",
      method: "GET",
    });
    result = await result.json();
    setUserData(result);
  }

  console.warn(trainigData);

  return (
    <div>
      <Header />
      <div className="col-sm-6 offset-sm-3">
        <h1> Price:</h1>
        <input
          type="text"
          defaultValue={trainigData.price}
          onChange={(e) => {
            setPrice(e.target.value);
          }}
        />{" "}
        <br /> <br />
        <h1> Amount of places:</h1>
        <input
          type="text"
          defaultValue={trainigData.free_places_amount}
          onChange={(e) => {
            setPlacesAmount(e.target.value);
          }}
        />{" "}
        <br />
        <input
          type="datetime-local"
          className="form-control"
          onChange={(e) => setBeginDate(e.target.value + ":00.000000Z")}
          placeholder="biegin date"
        />{" "}
        <br />
        <input
          type="datetime-local"
          className="form-control"
          onChange={(e) => setEndDate(e.target.value + ":00.000000Z")}
          placeholder="end date"
        />{" "}
        <br />
        <br />
        <input
          type="datetime-local"
          className="form-control"
          onChange={(e) =>
            setEnrolmentBeginDate(e.target.value + ":00.000000Z")
          }
          placeholder="enrolment begin date"
        />
        <br />
        <input
          type="datetime-local"
          className="form-control"
          onChange={(e) => setEnrolmentEndDate(e.target.value + ":00.000000Z")}
          placeholder="enrolment end date"
        />
        <h3>Choose City to burn</h3>
        <br />
        <select
          style={{ width: 300 }}
          value={place}
          onChange={(e) => setPlace([e.target.value])}
        >
          <option />
          {data.map((item) => (
            <option value={item.id}>
              {" "}
              {item.address}, {item.city.city}{" "}
            </option>
          ))}
        </select>
        <br />
        <br />
        <h3>Choose instructor for training</h3>
        <br />
        <select
          style={{ width: 300 }}
          value={instructor}
          onChange={(e) => setInstructor([e.target.value])}
        >
          <option />
          {userData.map((item) => (
            <option value={item.id}> {item.name} </option>
          ))}
        </select>
        <br />
        <br />
        <button onClick={updateTrainingFunc} className={"button"}>
          <span>Update Training</span>
        </button>
      </div>
    </div>
  );
}

export default withRouter(UpdateTraining);
