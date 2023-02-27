import React, { useState } from "react";
import FormComponent from "./FormComponent";

const MainPage = () => {
    const [pageData, setPageData] = useState({
        name: "",
        age: 0,
        date: "",
        programming: "",
        url:"",
    });

    const handleClick = () => {
        fetch("/data")
        .then(res => res.json())
        .then(
            (data) => {
                setPageData({
                    name: data.Name,
                    age: data.Age,
                    date: data.Date,
                    programming: data.programming,
                    url: data.url,
                });
            },
        )
    }
    
    
    return (
        <>
            <h1>SI699 Proj</h1>
            <FormComponent/>
            <button onClick={handleClick}>Show Results</button>

            {/* Calling a data from setdata for showing */}
            <p>{pageData.name}</p>
            <p>{pageData.age}</p>
            <p>{pageData.date}</p>
            <p>{pageData.programming}</p>
            <p>{pageData.url}</p>
        </>
    );
}

export default MainPage;