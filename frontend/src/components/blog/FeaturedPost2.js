import * as React from 'react';
import PropTypes from 'prop-types';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardActionArea from '@mui/material/CardActionArea';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { useState } from "react";
import FormComponent from "./FormComponent";


function FeaturedPost2(props) {
    const { post } = props;
    const [formData, setFormData] = useState({
        newURL: '',
        selectValue: "1",
    });
    // const [formData, setFormData] = useState({});
    // const [selectValue, setSelectValue] = useState('');

    const handleTextInputChange = (event) => {
        setFormData({ ...formData, newURL: event.target.value });
      };
    
    const handleSelectChange = (event) => {
        setFormData({ ...formData, selectValue: event.target.value });
    };
    

    // const handleSelectChange=(event)=>{
    //     const { name, value } = event.target;
    //     setFormData({ [name]: value});
    // };

    const handleClick = (event) => {
        event.preventDefault();
        console.log(formData);
        fetch('/submit-newURL', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),

        })
        .then((response) => {
            response.json();
        })
    };

    // console.log(selection);
    return (
        <Grid item xs={12} md={6}>
            <CardActionArea component="a" href="#">
                <Card sx={{ display: 'flex' }}>
                    <CardContent sx={{ flex: 1 }}>
                        <Typography component="h2" variant="h5">
                            {post.title}
                        </Typography>
                        <Typography variant="subtitle1" color="text.secondary">
                            {post.date}
                        </Typography>
                        <Typography variant="subtitle1" paragraph>
                            {post.description}
                        </Typography>

                        <form onSubmit={handleClick}>
                            <input
                                type = "text"
                                name = "newURL"
                                value = {formData.newURL|| ''}
                                onChange = {handleTextInputChange}
                                placeholder = "Enter your url"
                            />

                            <select id="selectValue" value={formData.selectValue} onChange={handleSelectChange}>
                                <option value="1">Phishing</option>
                                <option value="0">Not-Phishing</option>
                            </select>                        
                                                        
                            <button type = "submit">Submit</button>
                        </form>

                        {/* <p>{"thanks for submitting"}</p> */}
                    </CardContent>
                    <CardMedia
                    component="img"
                    sx={{ width: 160, display: { xs: 'none', sm: 'block' } }}
                    image={post.image}
                    alt={post.imageLabel}
                    />
                </Card>
            </CardActionArea>
        </Grid>
    );
}

FeaturedPost2.propTypes = {
    post: PropTypes.shape({
    date: PropTypes.string,
    description: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    imageLabel: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    }).isRequired,
};

export default FeaturedPost2;