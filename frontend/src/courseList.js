import Header from "./Header";
import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";
import { Link } from "react-router-dom";

function CourseList() {
  const [data, setData] = useState([]);
  const [searchTerm, setSearchTerm] = useState([]);
  const [searchTags, setSearchTags] = useState([]);

  useEffect(() => {
    async function fetchData() {
      let result = await fetch(
        "http://localhost:8080/courses?page=1&per_page=100",
        {
          credentials: "include",
          method: "GET",
        }
      );
      result = await result.json();
      setData(result.courses);
    }
    fetchData();
  }, []);

  return (
    <div>
      <Header />
      <div className="col-sm-6 offset-sm-3">
        <h1>Search Course</h1>
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
      <h1> Course list </h1>
      <Table>
        <thead>
          <tr>
            <td> Author </td>
            <td> Name </td>
            <td> Description </td>
            <td> Multimedias </td>
            <td> Tags </td>
            <td></td>
          </tr>
          {data
            .filter((val) => {
              if (searchTerm == "") {
                return val;
              } else if (
                val.name.toLowerCase().includes(searchTerm.toLowerCase())
              ) {
                return val;
              } else if (
                val.author.name.toLowerCase().includes(searchTerm.toLowerCase())
              ) {
                return val;
              } else if (
                val.description.toLowerCase().includes(searchTerm.toLowerCase())
              ) {
                return val;
              }
            })
            .map((item) => (
              <tr key={item.id}>
                <td> {item.author.name} </td>
                <td> {item.name} </td>
                <td> {item.description} </td>
                <td>
                  <td>
                    {" "}
                    {item.multimedias.slice(0, 1).map((allMultimedias) => (
                      <img
                        style={{ width: 100 }}
                        src={allMultimedias.filename}
                      />
                    ))}
                  </td>
                </td>

                <td>
                  {" "}
                  {item.tags
                    .filter((valTag) => {
                      if (searchTags == "") {
                        return valTag;
                      } else if (
                        valTag.name
                          .toLowerCase()
                          .includes(searchTags.toLowerCase())
                      ) {
                        return valTag;
                      }
                    })
                    ?.map((allTags) => allTags.name + " ")}
                </td>
                <td>
                  <Link to={"/updateProduct/" + item.id} className="link">
                    <span className="button">Update</span>
                  </Link>
                  <br /> <br />
                  <Link to={"/createTraining/" + item.id} className="link">
                    <span className="button">Create training</span>
                  </Link>
                </td>
              </tr>
            ))}
        </thead>
      </Table>
    </div>
  );
}

export default CourseList;
