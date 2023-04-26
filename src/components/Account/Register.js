import React, { useState } from 'react'
import Navbar from "../Landingpage/navbar";
import Footer from '../Landingpage/footer'
import './Account.css'

const Register = () => {
const [formValues, setFormValues] = useState({
username: '',
email: '',
password: '',
confirmPassword: ''
});

const handleChange = e => {
setFormValues({ ...formValues, [e.target.name]: e.target.value });
};

const handleSubmit = () => {
fetch('/register', {
method: 'POST',
headers: {
'Content-Type': 'application/json'
},
body: JSON.stringify(formValues)
});
};

const validateForm = () => {
return formValues.username && formValues.email && formValues.password && formValues.confirmPassword;
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
                Username:
            </label>
            <input name="username" value={formValues.username} onChange={handleChange} />
            
            <label>
                Email:
            </label>
            <input name="email" value={formValues.email} onChange={handleChange} />
            
            <label>
                Password:
            </label>
            <input type="password" name="password" value={formValues.password} onChange={handleChange} />
            
            <label>
                Confirm Password:
            </label>
            <input type="password" name="confirmPassword" value={formValues.confirmPassword} onChange={handleChange} />
            
            <button disabled={!validateForm()} onClick={handleSubmit} >Submit</button>
            <h4>Have an account? <a href="/login">Login Now!</a></h4>
        </form>
    </div>
    <Footer/>
</div>
)
}

export default Register