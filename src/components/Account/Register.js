import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import Navbar from '../Landingpage/navbar';
import Footer from '../Landingpage/footer';
import './Account.css';

const Register = () => {
  const [formValues, setFormValues] = useState({
    profile_image: null,
    firstName: '',
    lastName: '',
    email: '',
    password: '',
  });

  const handleChange = e => {
    if (e.target.name === 'profile_image') {
      setFormValues({ ...formValues, [e.target.name]: e.target.files[0] });
    } else {
      setFormValues({ ...formValues, [e.target.name]: e.target.value });
    }
  };

  const URL = 'https://woof-mates.onrender.com/auth/signup';

  const handleSubmit = async e => {
    e.preventDefault();

    try {
      const formData = new FormData();
      formData.append('profile_image', formValues.profile_image);
      formData.append('firstName', formValues.firstName);
      formData.append('lastName', formValues.lastName);
      formData.append('email', formValues.email);
      formData.append('password', formValues.password);

      const response = await axios.post(URL, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.status === 201) {
        // Handle the successful response here
        alert('User created successfully!');
        window.location.href = '/login';
      } else {
        // Handle errors
        alert('Error creating user.');
      }
    } catch (error) {
      // Handle network errors
      console.error('Network error:', error);
    }
  };

  const validateForm = () => {
    return formValues.email && formValues.password; // && formValues.confirmPassword;
  };

  return (
    <div>
      <Navbar />
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <label>
            <h1>Register</h1>
          </label>
          <br />
          <label>Profile Image:</label>
          <input
            type="file"
            name="profile_image"
            alt="profileImage"
            formEncType='multipart/form-data'
            onChange={handleChange}
          />
          <label>First Name:</label>
          <input name="firstName" value={formValues.firstName} onChange={handleChange} />
          <label>Last Name:</label>
          <input name="lastName" value={formValues.lastName} onChange={handleChange} />
          <label>Email:</label>
          <input name="email" value={formValues.email} onChange={handleChange} />
          <label>Password:</label>
          <input type="password" name="password" value={formValues.password} onChange={handleChange} />
          <button disabled={!validateForm()}>Submit</button>
          <h4>
            Have an account? <Link to="/login">Login Now!</Link>
          </h4>
        </form>
      </div>
      <Footer />
    </div>
  );
};

export default Register;

