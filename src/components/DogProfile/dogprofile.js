
import React, { useState } from "react";
import Navbar from "../Landingpage/navbar";
import axios from "axios";
import "./dogprofile.css"; // Import CSS file for styling
import preferenceOptions from "./preferenceOptions.json";
import breedOptions from './breedOptions.json';

export default function DogProfile() {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [breed, setBreed] = useState("");
  const [description, setDescription] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [country, setCountry] = useState("");
  const [relationshipPref, setRelationshipPref] = useState("");

  const [image1, setImage1] = useState(null);
  const [image2, setImage2] = useState(null);
  const [image3, setImage3] = useState(null);


  const handleImage1Change = (event) => {
    const reader = new FileReader();
    reader.onload = () => {
      if (reader.readyState === 2) {
        setImage1(reader.result);
      }
    };
    reader.readAsDataURL(event.target.files[0]);
  };

  const handleImage2Change = (event) => {
    const reader = new FileReader();
    reader.onload = () => {
      if (reader.readyState === 2) {
        setImage2(reader.result);
      }
    };
    reader.readAsDataURL(event.target.files[0]);
  };

  const handleImage3Change = (event) => {
    const reader = new FileReader();
    reader.onload = () => {
      if (reader.readyState === 2) {
        setImage3(reader.result);
      }
    };
    reader.readAsDataURL(event.target.files[0]);
  };





  const handleSubmit = async (event) => {
    event.preventDefault();

    // Create form data object to send to API
    const formData = new FormData();
    formData.append("name", name);
    formData.append("age", age);
    formData.append("breed", breed);
    formData.append("description", description);
    formData.append("city", city);
    formData.append("state", state);
    formData.append("country", country);
    formData.append("relationship_pref", relationshipPref);
    formData.append("image1", image1);
    formData.append("image2", image2);
    formData.append("image3", image3);

    try {
      // Send form data to API using Axios
      const response = await axios.post(
        "https://woof-mates.onrender.com/docs#/Dogs/create_profile_profile_create_dog_profile_post",
        formData
      );
      console.log(response.data); // Log API response data to console
    } catch (error) {
      console.error(error); // Log error to console
    }
  };

  return (
    <div>

    <Navbar /> 
    <div className="dog-profile-container">


      <h1>Create Your Dog's Profile</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name*</label>
          <input
            type="text"
            id="name"
            required
            value={name}
            onChange={(event) => setName(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="age">Age*</label>
          <input
            type="number"
            id="age"
            required
            value={age}
            onChange={(event) => setAge(event.target.value)}
          />
        </div>
       


        <div className="form-group">
      <label htmlFor="breed">Breed*</label>
      <select id="breed" value={breed} onChange={(event) => setBreed(event.target.value)}>
        <option value="">Select breed</option>
        {breedOptions.breeds.map((breed) => (
          <option key={breed} value={breed}>{breed}</option>
        ))}
      </select>
    </div>



        <div className="form-group">
          <label htmlFor="description">Description</label>
          <textarea
            id="description"
            value={description}
            onChange={(event) => setDescription(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="city">City*</label>
          <input
            type="text"
            id="city"
            required
            value={city}
            onChange={(event) => setCity(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="state">State*</label>
          <input
            type="text"
            id="state"
            required
            value={state}
            onChange={(event) => setState(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="country">Country*</label>
          <input
            type="text"
            id="country"
            required
            value={country}
            onChange={(event) => setCountry(event.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="relationshipPref">Relationship preference*</label>
          <select
            className="relationshipPref"
            id="relationshipPref"
            value={relationshipPref}
            onChange={(event) => setRelationshipPref(event.target.value)}
          >
            <option value="">Select preference</option>
            {preferenceOptions.preferences.map((preference) => (
              <option key={preference} value={preference}>
                {preference}
              </option>
            ))}
          </select>
        </div>


        <div className="dog-profile-container">
      <div className="image-container">
        <div className="image-wrapper">
          <img src={image1} alt="" className="dog-image" />
        </div>
        <input
          type="file"
          accept="image/*"
          onChange={handleImage1Change}
          className="image-input"
          placeholder="Input your image"
        />
      </div>
      <div className="image-container">
        <div className="image-wrapper">
          <img src={image2} alt="" className="dog-image" />
        </div>
        <input
          type="file"
          accept="image/*"
          onChange={handleImage2Change}
          className="image-input"
        />
      </div>
      <div className="image-container">
        <div className="image-wrapper">
          <img src={image3} alt="" className="dog-image" />
        </div>
        <input
          type="file"
          accept="image/*"
          onChange={handleImage3Change}
          className="image-input"
        />
      </div>
    </div>
      </form>
    </div>
    </div>
  );
}