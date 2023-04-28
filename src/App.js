import { AuthProvider } from './components/Account/AuthProvider';
import "./App.css";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Home from "./components/Landingpage/Home";
import HomeFeed from "./components/Dashboard/proto/Homefeed"; 
import Profile from "./components/Dashboard/Profile";
import Register from "./components/Account/Register";
import Login from "./components/Account/Login";
import ViewMatches from "./components/Dashboard/proto/ViewMatches"; // import the ViewMatches component

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route exact path="/homefeed" element={<HomeFeed/>} />
          <Route exact path="/profile" element={<Profile/>} />
          <Route exact path="/register" element={<Register/>} />
          <Route exact path="/login" element={<Login/>} />
          <Route exact path="/matches/:dogId" element={<ViewMatches/>} /> {/* add the route for the ViewMatches component */}
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;