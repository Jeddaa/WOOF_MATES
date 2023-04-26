import React, { useState } from 'react'
import axios from 'axios';
import Navbar from "../Landingpage/navbar";
import Footer from '../Landingpage/footer'
import './Account.css'

const Register = () => {
const [formValues, setFormValues] = useState({
profile_image: '',
firstName:'',
lastName:'',
email: '',
password: '',
});

const handleChange = e => {
setFormValues({ ...formValues, [e.target.name]: e.target.value });
};

const URL = 'https://woof-mates.onrender.com/auth/signup';

const handleSubmit = async () => {
    try {
      const formData = new FormData();
      formData.append('profile_image', formValues.profile_image);
      formData.append('firstName', formValues.firstName);
      formData.append('lastName', formValues.lastName);
      formData.append('email', formValues.email);
      formData.append('password', formValues.password);
  
      const response = await axios.post(URL, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
  
      if (response.status === 201) {
        // Handle the successful response here
        console.log('User created successfully!');
      } else {
        // Handle errors
        console.error('Error creating user.');
      }
    } catch (error) {
      // Handle network errors
      console.error('Network error:', error);
    }
  };

const validateForm = () => {
return formValues.email && formValues.password; // && formValues.confirmPassword;
}

return (
<div>
    <Navbar/>
    <div className='form-container'>
        <form>
            <label>
                <h1>Register</h1>
            </label>
            <br />
            <label>
                Profile Image:
            </label>
            <input type="file" name="profile_image" alt="profileImage" value={formValues.profile_image} onChange={handleChange} />
            <label>
                First Name:
            </label>
            <input name="firstName" value={formValues.firstName} onChange={handleChange} />
            <label>
                Last name:
            </label>
            <input name="lastName" value={formValues.lastName} onChange={handleChange} />
            {/* <label>
                Username:
            </label>
            <input name="username" value={formValues.username} onChange={handleChange} /> */}
           
            <label>
                Email:
            </label>
            <input name="email" value={formValues.email} onChange={handleChange} />
            
            <label>
                Password:
            </label>
            <input type="password" name="password" value={formValues.password} onChange={handleChange} />
            
            <button disabled={!validateForm()} onClick={handleSubmit} >Submit</button>
            <h4>Have an account? <a href="/login">Login Now!</a></h4>
        </form>
    </div>
    <Footer/>
</div>
)
}

export default Register