import React from "react";
import Hero from "./hero";
import Footer from "./footer";
import Navbar from "./navbar";
import Features from "./features";
import Form from "./form";
import Snap from "./../../img/snap.png";

function Home() {

  const options = [
    { value: "green", label: "Green" },
    { value: "blue", label: "Blue" },
    { value: "red", label: "Red" },
    { value: "yellow", label: "Yellow" },
    { value: "orange", label: "Orange" },
    { value: "pink", label: "Pink" },
    { value: "purple", label: "Purple" },
    { value: "grey", label: "Grey" },
  ];
  
  return (
    <div>
      <Navbar />
      <Hero />
      <div className="img_section_div">
    <img src={Snap} alt="" className="img_section" />
    </div>
      <Features />
      <Form />
      <Footer />
    </div>
  );
}

export default Home;
