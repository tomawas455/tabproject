import Header from "./Header";
import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";
import Multiselect from "multiselect-react-dropdown";

function RaportsForWorker() {
    const [data, setData] = useState([]);
    const [fromDate, setFromDate] = useState([]);
    const [courseData, setCourseData] = useState([]);
    const [courseInfo, setCourseInfo] = useState([]);
   // const [authorData, setAuthorData] = useState([]);
   // const [authorInfo, setAuthorInfo] = useState([]);
    const [trainingData, setTrainingData] = useState([]);
    const [trainingInfo, setTrainingInfo] = useState([]);
    const [toDate, setToDate] = useState([]);

    useEffect(() => {
        getCourses();
        getTraining();
    }, []);

    async function getCourses() {
        let result = await fetch("http://localhost:8080/courses?page=1&per_page=100", {
            credentials: "include",
            method: "GET",
        });
        result = await result.json();
        setCourseData(result);
        //setAuthorData(result.courses);
    }


    async function getTraining() {
        let result = await fetch("http://localhost:8080/trainings/?=&=&=&=&=&=", {
            credentials: "include",
            method: "GET",
        });
        result = await result.json();
        setTrainingData(result.trainings);
    }

    async function Find() {
        let result = await fetch(
            "http://localhost:8080/raports/worker",
            {
                credentials: "include",
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify({
                    from_date: fromDate,
                    to_date: toDate,
                    courses: courseInfo,
                    trainings: trainingInfo,
                   // authors: authorInfo,
                }),
            }
        );
        result = await result.json();
        setData(result.trainings);
    }


        console.warn(data);



    return (
        <div>
            <Header />
            <div>
                <h1>Date from:</h1>
                <input
                    type="datetime-local"
                    className="form-control"
                    onChange={(e) => setFromDate(e.target.value + ":00.000000Z")}
                    placeholder="from date"
                />
                <h1>Date to:</h1>
                <input
                    type="datetime-local"
                    className="form-control"
                    onChange={(e) => setToDate(e.target.value + ":00.000000Z")}
                    placeholder="to date"
                />
                <h1> Course: </h1>
                <Multiselect
                    onRemove={(e)=> setCourseInfo(e.map((item) => item.id))}
                    onSelect={(e) => setCourseInfo(e.map((item) => item.id))}
                    options={courseData.courses}
                    displayValue={"name"}
                />
                {/*<h1> Author: </h1>
                <Multiselect
                    key = {authorData.map((item)=>item.author)}
                    onRemove={(e)=> setAuthorInfo(e.map((item) => item.id))}
                    onSelect={(e) => setAuthorInfo(e.map((item) => item.id))}
                    options={authorData.map((item)=>item.author)}
                    displayValue={"name"}
                />*/}
                <h1> Training: </h1>
                <Multiselect
                    onRemove={(e)=> setTrainingInfo(e.map((item) => item.id))}
                    onSelect={(e) => setTrainingInfo(e.map((item) => item.id))}
                    options={trainingData.map((item)=>item.course)}
                    displayValue={"name"}
                />
                <button onClick={Find} className={"button"}>
                    <span>Find</span>
                </button>
                <Table>
                    <thead>
                    <tr>
                        <td> Name </td>
                        <td> Price </td>
                        <td> How many sold</td>
                        <td> Income </td>
                        <td> Expense</td>
                    </tr>

                    {data.map((item)=> (
                        <tr>
                            <td>{item.course.name}</td>
                            <td>{item.price}</td>
                            <td>{item.places_amount-item.free_places_amount}</td>
                            <td>{item.income}</td>
                            <td>{item.course.expense}</td>
                        </tr>
                    ))}

                    </thead>
                </Table>
            </div>
        </div>
    );
}

export default RaportsForWorker;
