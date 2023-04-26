import "./App.css";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Home from "./components/Landingpage/Home";
import HomeFeed from "./components/Dashboard/Homefeed"; 
import Profile from "./components/Dashboard/Profile";
import Register from "./components/Account/Register";
import Login from "./components/Account/Login";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route exact path="/homefeed" element={<HomeFeed/>} />
        <Route exact path="/profile" element={<Profile/>} />
        <Route exact path="/register" element={<Register/>} />
        <Route exact path="/login" element={<Login/>} />
      </Routes>
    </Router>
  );
}

export default App;
