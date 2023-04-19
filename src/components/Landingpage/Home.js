import React from "react";
import Hero from "./hero";
import Footer from "./footer";
import Navbar from "./navbar";
import Features from "./features";

function Home() {
  return (
    <div>
      <Navbar />
      <Hero />
      <Features />
      <Footer />
    </div>
  );
}

export default Home;
