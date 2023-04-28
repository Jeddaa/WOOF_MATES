import { AuthProvider } from './components/Account/AuthProvider';
import "./App.css";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Home from "./components/Landingpage/Home";
import Profile from "./components/Dashboard/Profile";
import Register from "./components/Account/Register";
import Login from "./components/Account/Login";
import Contact from "./contactus";
import About from "./about";
import Chat from "./components/chat";
import DogProfile from "./components/DogProfile/dogprofile";


function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route exact path="/profile" element={<Profile/>} />
          <Route exact path="/dogprofile" element={<DogProfile/>} />
          <Route exact path="/register" element={<Register/>} />
          <Route exact path="/login" element={<Login/>} />
          <Route path="/about" element={<About />} />
          <Route path="/contactus" element={<Contact />} />
          <Route path="/chat" element={<Chat />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;