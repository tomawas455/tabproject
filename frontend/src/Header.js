import { Navbar, Nav, NavDropdown } from "react-bootstrap";
import { Container } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import React, { useState } from "react";
import logo from "./images/logo.png";

function Header() {
  let user = JSON.parse(localStorage.getItem("user-info"));
  const navigate = useNavigate();

  function logOut() {
    localStorage.clear();
    navigate("/login");
  }

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
                <Link to="/" className="link">
                  {" "}
                  Courses{" "}
                </Link>
                <Link to="/trainingList" className="link">
                  {" "}
                  Trainings{" "}
                </Link>
                <Link to="/createCourseForWorker" className="link">
                  {" "}
                  Create course{" "}
                </Link>
                <Link to="/GetUsers" className="link">
                  {" "}
                  Users{" "}
                </Link>
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
