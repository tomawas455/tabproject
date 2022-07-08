import Header from "./Header";
import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";

function RaportsForUser() {
    const [data, setData] = useState([]);
    const [fromDate, setFromDate] = useState([]);
    const [toDate, setToDate] = useState([]);



    async function Find() {
        let result = await fetch(
            "http://localhost:8080/raports/user",
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
                }),
            }
        );
        result = await result.json();
        setData(result.trainings);
    }

    console.warn(JSON.stringify({
        from_date: fromDate,
        to_date: toDate,
    }));

    console.warn(fromDate);
    console.warn(toDate);
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
                <button onClick={Find} className={"button"}>
                    <span>Find</span>
                </button>
                <Table>
                    <thead>
                        <tr>
                            <td> Name </td>
                            <td> Price </td>
                        </tr>

                        {data.map((item)=> (
                            <tr>
                            <td>{item.course.name}</td>
                            <td>{item.price}</td>
                            </tr>
                        ))}

                    </thead>
                </Table>
            </div>
        </div>
    );
}

export default RaportsForUser;
