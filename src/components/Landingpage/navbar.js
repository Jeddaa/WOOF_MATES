// import Link from 'react'
import Logo from "./../../img/logo.webp";
import { Link, NavLink } from "react-router-dom";
import { useState } from "react";

export default function Navbar() {
  const [isActive, setIsActive] = useState(true);

  const hideHamburger = () => {
    setIsActive((current) => !current);
  };

  return (
    <div className=" bg-white nav_bar">
      <div className="d-flex p-3 align-items-center justify-content-between nav_b">
        {/* logo */}
        {isActive ? (
          <div>
            <Link to="/">
              <img src={Logo} alt="" className="logo" />
            </Link>
          </div>
        ) : (
          ""
        )}

        {/* hamburger */}
        <div className="navbar navbar-dark d-grid d-md-none">
          {/* <div className="container"> */}

          {/* hamburger button*/}
          <button
            className="navbar-toggler ms-auto"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#n_bar"
            aria-controls="navbarNavAltMarkup"
            aria-label="Toggle navigation"
            style={{
              display: isActive ? "block" : "none",
            }}
            onClick={hideHamburger}
          >
            <span className="navbar-toggler-icon bg-dark rounded-3 "></span>
          </button>
        </div>
        {/* </div> */}

        {/* widescreen navbar options */}
        <div className="d-none d-md-block">
          <ul className="Nav_1">
            <li>
              <NavLink
                to="/"
                className="text-decoration-none nav_link"
                id="nav_link"
                activeClassName="active"
              >
                Home
              </NavLink>
            </li>
            <li>
              <NavLink
                to="/about"
                className="text-decoration-none nav_link"
                id="nav_link"
                activeClassName="active"
              >
                About
              </NavLink>
            </li>
            <li>
              <NavLink
                to="/contactus"
                className="text-decoration-none nav_link"
                id="nav_link"
                activeClassName="active"
              >
                Contact Us
              </NavLink>
            </li>
            <li>
              <NavLink
                to="/login"
                className="text-decoration-none nav_link"
                id="nav_link"
                activeClassName="active"
              >
                Dashboard
              </NavLink>
            </li>
          </ul>
        </div>

        <Link
          to="login"
          className="btn button-primary bg-black text-white rounded-pill px-5 d-none  d-md-block"
        >
          Sign-in
        </Link>
      </div>

      {/* hanburger navbar options */}
      {!isActive ? (
        <div className="nav-options close d-md-none">
          <ion-icon
            name="close-circle-outline"
            size="large"
            onClick={hideHamburger}
          ></ion-icon>
          <img src={Logo} alt="" className="logo" />
          <ul className="Nav_">
            <li>
              <Link to="/" className="text-decoration-none nav_link">
                Home
              </Link>
            </li>
            <li>
              <Link to="/about" className="text-decoration-none nav_link">
                About
              </Link>
            </li>
            <li>
              <Link to="/contactus" className="text-decoration-none nav_link">
                Contact Us
              </Link>
            </li>
            <li>
              <Link
                to="/login"
                className="text-decoration-none nav_link"
                id="nav_link"
                activeClassName="active"
              >
                Dashboard
              </Link>
            </li>
          </ul>

          <Link
            to="login"
            className="btn button-primary bg-black text-white rounded-pill px-5"
            id="btnn"
          >
            Sign-in
          </Link>
        </div>
      ) : (
        ""
      )}
    </div>
  );
}
