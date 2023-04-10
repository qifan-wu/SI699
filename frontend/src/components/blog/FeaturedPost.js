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


function FeaturedPost(props) {
    const { post } = props;
    const [pageData, setPageData] = useState({
        name: "",
        age: 0,
        date: "",
        programming: "",
        url:"",
        label:"",
    });
    const [formData, setFormData] = useState({});
    const [showPopup, setShowPopup] = useState(false);

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormData({ [name]: value });
    };
    const handleClick = (event) => {
        event.preventDefault();
        setShowPopup(true);
        fetch('/submit-form', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
        })
        .then((response) => {
            response.json();
        })
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
                    label: data.label,
                });
            },
        )
    };
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
                                name = "url"
                                value = {formData.url || ''}
                                onChange = {handleInputChange}
                                placeholder = "Url"
                            />
                            <button type = "submit">Submit</button>
                        </form>
                        {showPopup && (
                            <div className="popup">
                            <p>{pageData.label=="1"?"phishing":"not phishing"}</p>
                            </div>
                        )}
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

FeaturedPost.propTypes = {
    post: PropTypes.shape({
    date: PropTypes.string,
    description: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    imageLabel: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    }).isRequired,
};

export default FeaturedPost;
