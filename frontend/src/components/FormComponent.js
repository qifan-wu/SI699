import React, { useState } from 'react';

function FormComponent() {
    const [formData, setFormData] = useState({});

    const handleSubmit = (event) => {
        event.preventDefault();
        fetch('/submit-form', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
        })
        .then((response) => response.json())
    };

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormData({ ...formData, [name]: value });
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
