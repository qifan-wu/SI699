import React, { useState } from 'react';

const FormComponent = () => {
    const [formData, setFormData] = useState({});

    const handleSubmit = (event) => {
        console.log("---------before submit");
        console.log(formData);
        event.preventDefault();
        fetch('/submit-form', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
        })
        .then((response) => {
            response.json();
            console.log("---------after submit");
            console.log(formData);
        })
    };

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormData({ [name]: value });
        console.log("----------handleInputChange")
        console.log(formData);
    };



    return (
        <form onSubmit={handleSubmit}>
        <input
            type = "text"
            name = "url"
            value = {formData.url || ''}
            onChange = {handleInputChange}
            placeholder = "Url"
        />
        <button type = "submit">Submit</button>
        </form>
    );
}

export default FormComponent;
