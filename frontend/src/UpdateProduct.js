import Header from "./Header";
import React, { useState, useEffect } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import Multiselect from "multiselect-react-dropdown";

function withRouter(Component) {
  function ComponentWithRouterProp(props) {
    let location = useLocation();
    let navigate = useNavigate();
    let params = useParams();
    return <Component {...props} router={{ location, navigate, params }} />;
  }

  return ComponentWithRouterProp;
}

function UpdateProduct(props) {
  const [data, setData] = useState([]);
  const [tagData, setTagData] = useState([]);
  const [name, setName] = useState([]);
  const [description, setDescription] = useState([]);
  const [tags, setTags] = useState([]);
  const [expense, setExpense] = useState("");

  useEffect(() => {
    getData();
    getTag();
  }, [props]);


  async function updateProduct(id) {
    let item = { name, description, tags, expense };
    console.warn("item", item);
    await fetch("http://localhost:8080/courses/" + id + "/edit", {
      method: "PATCH",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(item),
    }).then((response) => {
      if (response.statusText === "BAD REQUEST") {
        console.warn(response);
        alert("Someone already enroled on this course!", "Title");
        throw new Error("Bad response from server");
      }
      alert("Sucessfuly updated couse !");
    });
  }

  async function getData() {
    let result = await fetch(
      "http://localhost:8080/courses/" + props.router.params.id,
      {
        credentials: "include",
        method: "GET",
      }
    );
    result = await result.json();
    setData(result);
  }

  async function getTag() {
    let result = await fetch("http://localhost:8080/tags", {
      credentials: "include",
      method: "GET",
    });
    result = await result.json();
    setTagData(result);
  }

  return (
    <div>
      <Header />
      <div className="col-sm-6 offset-sm-3">
        <h1> New name:</h1>
        <input
          type="text"
          value={name}
          onChange={(e) => {
            setName(e.target.value);
          }}
        />{" "}
        <br /> <br />
        <h1> New description:</h1>
        <input
          type="text"
          value={description}
          onChange={(e) => {
            setDescription(e.target.value);
          }}
        />{" "}
        <br /> <br />
        <h1> New tags:</h1>
        {/*<select value={tags} onChange={(e) => setTags([e.target.value])}>
          <option />
          {tagData.map((item) => (
            <option value={item.id}> {item.name} </option>
          ))}
        </select>*/}
        <Multiselect
          onSelect={(e) => setTags(e.map((item) => item.id))}
          options={tagData}
          displayValue={"name"}
        />
        <br />
        <br />
        <h1> New Expense:</h1>
        <input
          type="text"
          value={expense}
          onChange={(e) => {
            setExpense(e.target.value);
          }}
        />{" "}
        <br /> <br />
        <button onClick={() => updateProduct(data.id)} className={"button"}>
          <span>Update Product</span>
        </button>
      </div>
    </div>
  );
}

export default withRouter(UpdateProduct);
