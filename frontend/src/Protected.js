import React, { useState, useEffect } from "react";
import Header from "./Header";
import { useNavigate } from "react-router-dom";

function Protected(props) {
  const navigate = useNavigate();

  let Cmp = props.Cmp;
  useEffect(() => {
    if (!localStorage.getItem("user-info")) {
      navigate("/login");
    }
    console.warn(localStorage);
  }, []);

  return (
    <div>
      <Cmp />
    </div>
  );
}

export default Protected;
