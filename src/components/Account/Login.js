import React, { useContext, useState } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from './AuthProvider';
import Navbar from '../Landingpage/navbar';
import Footer from '../Landingpage/footer';
import './Account.css';

const Login = () => {
  const [formValues, setFormValues] = useState({
    email: '',
    password: '',
  });

  const { login } = useContext(AuthContext);

  const handleChange = e => {
    setFormValues({ ...formValues, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();

    try {
      const success = await login(formValues.email, formValues.password);
      if (success) {
        // Redirect to home feed
        window.location.href = '/profile';
      } else {
        alert('Failed to login. Please try again.');
      }
    } catch (error) {
      // Display error message to user
      console.error(error);
      alert('Failed to login. Please try again.');
    }
  };

  const isFormValid = () => {
    return formValues.email && formValues.password;
  };

  return (
    <div>
      <Navbar />
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <label>
            <h1>Login</h1>
          </label>
          <br />
          <label>
            Email:
            <input
              name="email"
              value={formValues.email}
              onChange={handleChange}
            />
          </label>
          <label>
            Password:
            <input
              type="password"
              name="password"
              value={formValues.password}
              onChange={handleChange}
            />
          </label>
          <button disabled={!isFormValid()}>Submit</button>
          <h4>
            Don't have an account? <Link to="/register">Sign up now!</Link>
          </h4>
        </form>
      </div>
      <Footer />
    </div>
  );
};

export default Login;













// import React, { useState } from 'react';
// import { Link } from 'react-router-dom';
// import axios from 'axios';
// import qs from 'qs';
// import Navbar from '../Landingpage/navbar';
// import Footer from '../Landingpage/footer';
// import './Account.css';

// const Login = () => {
//   const [formValues, setFormValues] = useState({
//     email: '',
//     password: '',
//   });

//   const handleChange = e => {
//     setFormValues({ ...formValues, [e.target.name]: e.target.value });
//   };

//   const URL = 'https://woof-mates.onrender.com/auth/login';

//   const handleSubmit = async e => {
//     e.preventDefault();

//     try {
//       const formData = qs.stringify(formValues);
//       const response = await axios.post(URL, formData, {
//         headers: {
//           'Content-Type': 'application/x-www-form-urlencoded',
//         },
//       });
//       if (response.status === 200) {
//         // Store the access token in local storage
//         localStorage.setItem('access_token', response.data.access_token);

//         // Redirect to home feed
//         window.location.href = '/profile';
//       }
//     } catch (error) {
//       // Display error message to user
//       console.error(error);
//       alert('Failed to login. Please try again.');
//     }
//   };

//   const isFormValid = () => {
//     return formValues.email && formValues.password;
//   };

//   return (
//     <div>
//       <Navbar />
//       <div className="form-container">
//         <form onSubmit={handleSubmit}>
//           <label>
//             <h1>Login</h1>
//           </label>
//           <br />
//           <label>
//             Email:
//             <input
//               name="email"
//               value={formValues.email}
//               onChange={handleChange}
//             />
//           </label>
//           <label>
//             Password:
//             <input
//               type="password"
//               name="password"
//               value={formValues.password}
//               onChange={handleChange}
//             />
//           </label>
//           <button disabled={!isFormValid()}>Submit</button>
//           <h4>
//             Don't have an account? <Link to="/register">Sign up now!</Link>
//           </h4>
//         </form>
//       </div>
//       <Footer />
//     </div>
//   );
// };

// export default Login;