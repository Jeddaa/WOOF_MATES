import { createContext, useState } from 'react';
import axios from 'axios';

export const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  function login(email, password) {
    const URL = 'https://woof-mates.onrender.com/auth/login';

    const formData = new FormData();
    formData.append('email', email);
    formData.append('password', password);

    return axios.post(URL, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    }).then(response => {
      const token = response.data.access_token;
      localStorage.setItem('access_token', token);
      setUser({ email, token });
      return true;
    }).catch(error => {
      console.error(error);
      return false;
    });
  }

  function logout() {
    localStorage.removeItem('access_token');
    setUser(null);
  }

  const authContextValue = {
    user,
    login,
    logout,
  };

  return (
    <AuthContext.Provider value={authContextValue}>
      {children}
    </AuthContext.Provider>
  );
}