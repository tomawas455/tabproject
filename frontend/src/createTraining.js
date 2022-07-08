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

function CreateTraining(props) {
  const [userData, setUserData] = useState([]);
  const [data, setData] = useState([]);
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
  }, []);

  async function cities() {
    let result = await fetch("http://localhost:8080/places", {
      credentials: "include",
      method: "GET",
    });
    result = await result.json();
    setData(result);
  }

  async function getUserData() {
    let result = await fetch("http://localhost:8080/users/role/2", {
      credentials: "include",
      method: "GET",
    });
    result = await result.json();
    setUserData(result);
  }

  async function addCourse() {
    let result = await fetch("http://localhost:8080/trainings", {
      method: "POST",
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
        course_id: props.router.params.id,
        place_id: place,
        instructor_id: instructor,
      }),
    });
    result = await result.json();
  }

  return (
    <div>
      <Header />
      <div className="col-sm-6 offset-sm-3">
        <br />
        <input
          type="text"
          className="form-control"
          onChange={(e) => setPrice(e.target.value)}
          placeholder="price"
        />{" "}
        <br />
        <input
          type="text"
          className="form-control"
          onChange={(e) => setPlacesAmount(e.target.value)}
          placeholder="amount of places"
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
        <button onClick={addCourse} className="button">
          <span>Add course</span>
        </button>
      </div>
    </div>
  );
}

export default withRouter(CreateTraining);
