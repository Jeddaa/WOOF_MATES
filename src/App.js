import "./App.css";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Home from "./components/Landingpage/Home";
import HomeFeed from "./components/Dashboard/Homefeed"; 

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/homefeed" element={<HomeFeed/>}/>
      </Routes>
    </Router>
  );
}

export default App;
