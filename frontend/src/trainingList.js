import Header from "./Header";
import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";
import { Link } from "react-router-dom";

function TrainingList() {
  const [data, setData] = useState([]);
  const [searchTerm, setSearchTerm] = useState([]);
  const [searchTags, setSearchTags] = useState([]);

  useEffect(() => {
    async function fetchData() {
      let result = await fetch("http://localhost:8080/trainings/?=&=&=&=&=&=", {
        credentials: "include",
        method: "GET",
      });
      result = await result.json();
      setData(result.trainings);
    }
    fetchData();
  }, []);

  console.warn(data);

  return (
    <div>
      <Header />
      <div className="col-sm-6 offset-sm-3">
        <h1>Search Training</h1>
        <br />
        <input
          type="text"
          placeholder="Search..."
          onChange={(e) => {
            setSearchTerm(e.target.value);
            setSearchTags(e.target.value);
          }}
          className="form-control"
        />
      </div>
      <h1> Training list </h1>
      <Table>
        <thead>
          <tr>
            <td> Author </td>
            <td> Name </td>
            <td> Description </td>
            <td> Tags </td>
            <td> Expense </td>
            <td> Instructor </td>
            <td> Place </td>
            <td> City </td>
            <td> Amount of places</td>
            <td> </td>
            <td></td>
          </tr>
          {data.map((item) => (
            <tr key={item.id}>
              <td> {item.author.name} </td>
              <td> {item.course.name} </td>
              <td> {item.course.description} </td>
              <td> {item.course.tags.map((allTags) => allTags.name + " ")} </td>
              <td> {item.price + " $"} </td>
              <td> {item.instructor.name} </td>
              <td> {item.place.address} </td>
              <td> {item.place.city.city} </td>
              <td> {item.places_amount} </td>
              <td>
                <Link to={"/moreInfoAboutTraining/" + item.id}>
                  <span className="moreInfo">More info!</span>
                </Link>
              </td>
            </tr>
          ))}
        </thead>
      </Table>
    </div>
  );
}

export default TrainingList;
