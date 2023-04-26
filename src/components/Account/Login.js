import React, { useState } from 'react'
import Navbar from "../Landingpage/navbar";
import Footer from '../Landingpage/footer'
import './Account.css'

const Login = () => {
const [formValues, setFormValues] = useState({
email: '',
password: ''
});

const handleChange = e => {
setFormValues({ ...formValues, [e.target.name]: e.target.value });
};

const URL = 'https://woof-mates.onrender.com/docs#/User%20Routes/create_user_auth_signup_post';

const handleSubmit = () => {
fetch(URL, {
method: 'POST',
headers: {
'Content-Type': 'application/json'
},
body: JSON.stringify(formValues)
});
};




const validateForm = () => {
return formValues.email && formValues.password;
}

return (
<div>
<Navbar/>
<div className='form-container'>
<form>
<label>
<h1>Login</h1>
</label>
<br />
<label>
Email:
<input name="email" value={formValues.email} onChange={handleChange} />
</label>
<label>
Password:
<input type="password" name="password" value={formValues.password} onChange={handleChange} />
</label>
<button disabled={!validateForm()} onClick={handleSubmit} >Submit</button>
<h4>Don't have an account? <a href="/register">SignUp Now!</a></h4>
</form>
</div>
<Footer/>
</div>
)
}

export default Login