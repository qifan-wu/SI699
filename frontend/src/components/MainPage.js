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

    return (
        <>
            <h1>SI699 Proj</h1>
            {/* Calling a data from setdata for showing */}
            <p>{pageData.name}</p>
            <p>{pageData.age}</p>
            <p>{pageData.date}</p>
            <p>{pageData.programming}</p>
            <FormComponent/>
            <p>{pageData.url}</p>
        </>
    );
}

export default MainPage;