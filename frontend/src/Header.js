import { Navbar, Nav, NavDropdown } from "react-bootstrap";
import { Container } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import React, { useEffect, useState } from "react";
import logo from "./images/logo.png";

function Header() {
  let user = JSON.parse(localStorage.getItem("user-info"));
  const navigate = useNavigate();
  const [data, setData] = useState("");

  function logOut() {
    localStorage.clear();
    navigate("/login");
  }

  useEffect(() => {
    async function fetchData() {
      let result = await fetch("http://localhost:8080/users/current", {
        credentials: "include",
        method: "GET",
      });
      result = await result.json();
      setData(result.role.name);
    }
    fetchData();
  }, []);

  return (
    <div>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="/login">
            <img src={logo} alt="logo" width="120" />
          </Navbar.Brand>
          <Nav className="me-auto navbar_wrapper">
            {localStorage.getItem("user-info") ? (
              <>
                {data === "worker" ? (
                  <Link to="/" className="link">
                    {" "}
                    Courses{" "}
                  </Link>
                ) : null}
                <Link to="/trainingList" className="link">
                  {" "}
                  Trainings{" "}
                </Link>
                {data === "worker" ? (
                  <Link to="/createCourseForWorker" className="link">
                    {" "}
                    Create course{" "}
                  </Link>
                ) : null}
                {data === "user" ? (
                    <Link to="/raports" className="link">
                      {" "}
                      Raports{" "}
                    </Link>
                ) : null}
                {data === "worker" ? (
                    <Link to="/raportsForWorker" className="link">
                      {" "}
                      Raports{" "}
                    </Link>
                ) : null}
                {data === "administrator" ? (
                  <Link to="/GetUsers" className="link">
                    {" "}
                    Users{" "}
                  </Link>
                ) : null}
              </>
            ) : (
              <>
                <Link to="/login" className="link">
                  {" "}
                  Login{" "}
                </Link>
                <Link to="/register" className="link">
                  {" "}
                  Register{" "}
                </Link>
              </>
            )}
          </Nav>
          {localStorage.getItem("user-info") ? (
            <Nav>
              <NavDropdown title={user && user.name}>
                <NavDropdown.Item onClick={logOut}>Logout</NavDropdown.Item>
              </NavDropdown>
            </Nav>
          ) : null}
        </Container>
      </Navbar>
    </div>
  );
}

export default Header;
