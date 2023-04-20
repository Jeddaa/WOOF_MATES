import "./App.css";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Home from "./components/Landingpage/Home";
import HomeFeed from "./components/Dashboard/Homefeed"; 
import Profile from "./components/Dashboard/Profile";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/homefeed" element={<HomeFeed/>}/>
        <Route exact path="/profile" element={<Profile/>} />
      </Routes>
    </Router>
  );
}

export default App;
