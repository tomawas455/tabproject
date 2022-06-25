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
    const [price, setPrice]= useState([])
    const [placesAmount, setPlacesAmount]= useState([]);
    const [beginDate, setBeginDate]= useState([]);
    const [endDate, setEndDate]= useState([]);
    const [enrolmentBeginDate, setEnrolmentBeginDate]= useState([]);
    const [enrolmentEndDate, setEnrolmentEndDate]= useState([]);
    const [place, setPlace]= useState([]);
    const [instructor, setInstructor]= useState([]);
//TODO
    useEffect(() => {
        async function fetchData() {
            let result = await fetch("http://localhost:8080/places", {
                credentials: "include",
                method: "GET",
            });
            result = await result.json();
            setData(result);
        }
        fetchData();
    }, []);

    async function addCourse() {

        let result = await fetch("http://localhost:8080/courses/create", {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
                Accept: "application/json",
            },
            body: JSON.stringify({
            }),
        });
        result = await result.json();


    }

    console.warn(props);
    console.warn(data);


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
                    onChange={(e) => setBeginDate(e.target.value+":00.000000Z")}
                    placeholder="biegin date"
                />{" "}
                <br />
                <input
                    type="datetime-local"
                    className="form-control"
                    onChange={(e) => setEndDate(e.target.value+":00.000000Z")}
                    placeholder="end date"
                />{" "}
                <br />
                <br />
                <input
                    type="datetime-local"
                    className="form-control"
                    onChange={(e) => setEnrolmentBeginDate(e.target.value+":00.000000Z")}
                    placeholder="enrolment begin date"
                    />
                <br />
                <input
                    type="datetime-local"
                    className="form-control"
                    onChange={(e) => setEnrolmentEndDate(e.target.value+":00.000000Z")}
                    placeholder="enrolment end date"
                />
                <h3>Choose City to burn</h3>
                <br />
                <select style={{width:300}} value={place} onChange={(e) => setPlace([e.target.value])}>
                    <option/>
                    {data.map((item) => (
                        <option value={item.id}> {item.address}, {item.city.city} </option>
                    ))}
                </select>
                <br />
                <br />
                <button onClick={addCourse} className="btn btn-primary">
                    Add course
                </button>
            </div>
        </div>
    );
}

export default withRouter(CreateTraining);