import Header from "./Header";
import React, { useState, useEffect } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import { Link } from "react-router-dom";

function withRouter(Component) {
  function ComponentWithRouterProp(props) {
    let location = useLocation();
    let navigate = useNavigate();
    let params = useParams();
    return <Component {...props} router={{ location, navigate, params }} />;
  }

  return ComponentWithRouterProp;
}

function MoreInfoAboutTraining(props) {
  const [data, setData] = useState([]);
  const [dataV2, setDataV2] = useState([]);
  const [dataAddress, setDataAddress] = useState([]);
  const [dataCity, setDataCity] = useState([]);
  const [dataImage, setDataImage] = useState([]);
  const [text, setText] = useState([]);
  const [rate, setRate] = useState([]);
  const [amountOfPeople, setAmountOfPeople] = useState([]);

  useEffect(() => {
    getData();
  }, [props]);

  async function getData() {
    let result = await fetch(
      "http://localhost:8080/trainings/" + props.router.params.id,
      {
        credentials: "include",
        method: "GET",
      }
    );
    result = await result.json();
    setData(result);
    setDataV2(result.course);
    setDataAddress(result.place);
    setDataCity(result.place.city);
    setDataImage(result.course.multimedias);
  }

  let beginTime = new Date(data.begin_date);

  async function addComment() {
    let item = { text, rate };
    await fetch("http://localhost:8080/comments/" + props.router.params.id, {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        Accept: "application/json",
      },
      body: new URLSearchParams(item),
    });

    console.warn(text);
    console.warn(rate);
    console.warn(props.router.params.id);
  }

  let freePlacesAmount = data.free_places_amount;

  //TODO sprawdzic komendy po dodaniu mozliwosci brania udzialu w kursie
  //TODO wiecej obrazkow ?

  console.warn(data);

  return (
    <div>
      <Header />
      <div className="container">
        <br />
        <h1 className="nameoftraining"> {dataV2.name} </h1>
        <br />
        <div className="barL">
          <p className={"dateandcity"}>
            <b>Data: </b>{" "}
            {beginTime.getFullYear() +
              "-" +
              (beginTime.getMonth() + 1) +
              "-" +
              beginTime.getDate() +
              " " +
              beginTime.getHours() +
              ":" +
              beginTime.getMinutes()}{" "}
            <br />
            <b>Miejsce:</b> {dataAddress.address} , {dataCity.city}{" "}
          </p>

          <h2 className={"dateandcity"}> Opis kursu: </h2>
          <p className={"description"}> {dataV2.description} </p>
        </div>
        <div className="barR">
          <img
            style={{ width: 420 }}
            src={dataImage.slice(0, 1).map((item) => item.filename)}
          />
          <br />
          <p className="price"> {data.price}$/person </p>
          <Link to={"/participationForm/" + data.id} className={"button"}>
            <span>Apply</span>
          </Link>
        </div>
        <div className="coments">
          <select value={rate} onChange={(e) => setRate([e.target.value])}>
            <option />
            <option value={1}> {1} </option>
            <option value={2}> {2} </option>
            <option value={3}> {3} </option>
            <option value={4}> {4} </option>
            <option value={5}> {5} </option>
          </select>
          <textarea
            type="text"
            className="form-control"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="What do you think, about this training?"
          />
          <button onClick={addComment} className={"button-long"}>
            <span> Add comment </span>
          </button>
          <Link to={"/UpdateTraining/" + data.id} className={"button"}>
            <span>Update </span>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default withRouter(MoreInfoAboutTraining);
