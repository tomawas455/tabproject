import Header from "./Header";
import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";

function GetUsers() {
  const [data, setData] = useState([]);
  const [role, setRole] = useState([]);

  useEffect(() => {
    getData();
  }, []);

  async function updateRole(id) {
    let result = await fetch(
      "http://localhost:8080/users/" + id + "/change_role",
      {
        method: "PATCH",
        credentials: "include",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
          Accept: "application/json",
        },
        body: new URLSearchParams({
          role_id: role,
        }),
      }
    );
    result = await result.json();
    console.warn(result);
    getData();
    console.log("id", id);
    console.log("role", role);
  }

  async function getData() {
    let result = await fetch(
      "http://localhost:8080/users/?page=1&per_page=100",
      {
        credentials: "include",
        method: "GET",
      }
    );
    result = await result.json();
    setData(result.users);
    setRole(result.roles);
  }

  return (
    <div>
      <Header />
      <div>
        <h1>Users:</h1>
        <Table>
          <thead>
            <tr>
              <td> Email </td>
              <td> Id </td>
              <td> Name </td>
              <td> Surname </td>
              <td> Role </td>
            </tr>
            {data.map((item) => (
              <tr>
                <td> {item.email} </td>
                <td> {item.id} </td>
                <td> {item.name} </td>
                <td> {item.surname} </td>
                <td> {item.role.name} </td>
                <td>
                  <select
                    value={role}
                    onChange={(e) => setRole([e.target.value])}
                  >
                    <option />
                    {role.map((roles) => (
                      <option value={roles.id}> {roles.name} </option>
                    ))}
                  </select>
                  <button
                    onClick={() => updateRole(item.id)}
                    className="btn btn-primary"
                  >
                    {" "}
                    Change Role{" "}
                  </button>
                </td>
              </tr>
            ))}
          </thead>
        </Table>
      </div>
    </div>
  );
}

export default GetUsers;
