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



function MoreInfoAboutTraining(props) {
    const [data, setData] = useState([]);
    const [dataV2, setDataV2] = useState([]);
    const [dataAddress, setDataAddress] = useState([]);
    const [dataCity, setDataCity] = useState([]);
    const [dataImage, setDataImage] = useState([]);
    const [text, setText] = useState([]);
    const [rate, setRate] = useState([]);


    useEffect( () => {
        getData();
    }, [props]);


    async function getData() {

        let result = await fetch(
            "http://localhost:8080/trainings/"+props.router.params.id ,
            {
                credentials: "include",
                method: "GET",
            }
        );
        result = await result.json();
        setData(result);
        setDataV2(result.course);
        setDataAddress(result.place);
        setDataCity(result.place.city);
        setDataImage(result.course.multimedias);

    }


    let beginTime = new Date(data.begin_date);

    async function addComment() {

        let result = await fetch("http://localhost:8080/comments/"+props.router.params.id, {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                Accept: "application/json",
            },
            body: new URLSearchParams({
                text: text,
                rate: rate,
            }),
        });
        result = await result.json();

        console.warn(text);
        console.warn(rate);
        console.warn(props.router.params.id);
    }

//TODO sprawdzic komendy po dodaniu mozliwosci brania udzialu w kursie

    return (
        <div>
            <Header />
            <div className="col-sm-6 offset-sm-3">

                        <div className={'tour-info'}>
                            <h1> {dataV2.name} </h1>
                            <h2 className={'border'} > {beginTime.getFullYear()+'-' + (beginTime.getMonth()+1) + '-'+beginTime.getDate() + ' '+beginTime.getHours()+ ':'+beginTime.getMinutes()} </h2>
                            <h2 className={'border'}> {dataAddress.address} , {dataCity.city} </h2>
                            <img style={{width: 500}} src={dataImage.map((item)=>item.filename)}/>
                            <h3 className={'border'}> {dataV2.description}</h3>
                            <h4 className={'tour-price'}> {data.price} $ </h4>
                            <textarea
                                type="text"
                                className="form-control"
                                onChange={(e) => setText(e.target.value)}
                                placeholder="What do you think, about this training?"
                            />
                            <select value={rate} onChange={(e) => setRate([e.target.value])}>
                                <option/>
                                <option value = {1}> {1} </option>
                                <option value = {2}> {2} </option>
                                <option value = {3}> {3} </option>
                                <option value = {4}> {4} </option>
                                <option value = {5}> {5} </option>

                            </select>
                            <br/>
                            <button onClick={addComment} className={"btn btn-primary"} > Add comment </button>

                        </div>


            </div>
        </div>
    );
}

export default withRouter(MoreInfoAboutTraining);