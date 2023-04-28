import "./App.css";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Home from "./components/Landingpage/Home";
import Chat from "./components/chat";
import HomeFeed from "./components/Dashboard/Homefeed"; 
import Profile from "./components/Dashboard/Profile";
import DogProfile from "./components/DogProfile/dogprofile";
import About from "./components/about";
import Contact from "./components/contactus";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/homefeed" element={<HomeFeed/>}/>
        <Route exact path="/profile" element={<Profile/>} />
        <Route exact path="/dogprofile" element={<DogProfile/>} />
        <Route path="/chat" element={<Chat />} />
        <Route path="/about" element={<About />} />
        <Route path="/contactus" element={<Contact />} />
      </Routes>
    </Router>
  );
}

export default App;
