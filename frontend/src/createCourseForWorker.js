import React, { useState, useEffect } from "react";
import Header from "./Header";
import Multiselect from "multiselect-react-dropdown";

function CreateCourseForWorker() {
  const [selects, setSelects] = useState();
  const [data, setData] = useState([]);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [expense, setExpense] = useState("");
  const [tags, setTags] = useState([]);
  const [multimedias, setMultimedias] = useState([]);
  let user = JSON.parse(localStorage.getItem("user-info"));

  useEffect(() => {
    async function fetchData() {
      let result = await fetch("http://localhost:8080/tags", {
        credentials: "include",
        method: "GET",
      });
      result = await result.json();
      setData(result);
    }
    fetchData();
  }, []);

  async function addCourse() {
    let items = { name, description, expense, tags, multimedias };
    console.warn(items);

    let result = await fetch("http://localhost:8080/courses/create", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        name: name,
        description: description,
        expense: expense,
        tags: tags,
        multimedias: multimedias,
      }),
    });
    result = await result.json();
    console.log("result", items);
    alert("You have correctly created course !");
  }

  return (
    <div>
      <Header />
      <div className="col-sm-6 offset-sm-3">
        <br />
        <input
          type="text"
          className="form-control"
          onChange={(e) => setName(e.target.value)}
          placeholder="name"
        />{" "}
        <br />
        <textarea
          type="text"
          className="form-control"
          onChange={(e) => setDescription(e.target.value)}
          placeholder="description"
        />{" "}
        <br />
        <input
          type="text"
          className="form-control"
          onChange={(e) => setExpense(e.target.value)}
          placeholder="expense"
        />{" "}
        <br />
        <h3>Choose your tag</h3>
        <br />
        <Multiselect
          onSelect={(e) => setTags(e.map((item) => item.id))}
          options={data}
          displayValue={"name"}
        />
        <br />
        <br />
        <input
          type="text"
          className="form-control"
          multiple
          onChange={(e) => setMultimedias([e.target.value])}
          placeholder="multimedias, as URL"
        />
        <br />
        <button onClick={addCourse} className="button">
          <span>Add course</span>
        </button>
      </div>
    </div>
  );
}

export default CreateCourseForWorker;
