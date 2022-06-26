import Header from "./Header";
import React, { useState, useEffect } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";

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
  const [name, setName] = useState([]);
  const [description, setDescription] = useState([]);
  const [tags, setTags] = useState([]);
  const [expense, setExpense] = useState("");

  useEffect(() => {
    getData();
  }, [props]);

  async function updateProduct(id) {
    let result = await fetch("http://localhost:8080/courses/" + id + "/edit", {
      method: "PATCH",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        name: name,
        description: description,
      }),
    });
    result = await result.json();
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




  return (
    <div>
      <Header />
      <div className="col-sm-6 offset-sm-3">
        <h1> Name:</h1>
        <input
          type="text"
          defaultValue={data.name}
          onChange={(e) => {
            setName(e.target.value);
          }}
        />{" "}
        <br /> <br />
        <h1> Description:</h1>
        <input
          type="text"
          defaultValue={data.description}
          onChange={(e) => {
            setDescription(e.target.value);
          }}
        />{" "}
        <br /> <br />
        <h1> Tags:</h1>
        {data.tags?.map((allTags) => (
          <h2> {allTags.name}</h2>
        ))}
        <button
          onClick={() => updateProduct(data.id)}
          className={"btn btn-primary"}
        >
          Update Product
        </button>
      </div>
    </div>
  );
}

export default withRouter(UpdateProduct);
