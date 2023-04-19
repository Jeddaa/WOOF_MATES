import Logo from "./../../img/logo.webp";
import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <div className="footer-bg mb-0">
      <div className="container footer_content">
        <Link to="/">
          <img src={Logo} alt="" className="logo1 mt-5 mb-3" />
        </Link>
        <div className="socials">
          <a href="" target="_blank">
            <ion-icon name="mail-outline" className="icon"></ion-icon>
          </a>
          <a href="" target="_blank">
            <ion-icon name="logo-facebook" className="icon"></ion-icon>
          </a>
          <a href="" target="_blank">
            <ion-icon name="logo-twitter" className="icon"></ion-icon>
          </a>
          <a href="" target="_blank">
            <ion-icon name="logo-instagram" className="icon"></ion-icon>
          </a>
        </div>
        <div className="footer_links ">
          <ul>
            <Link to="/" className="linkss">
              <li>Home</li>
            </Link>
            <Link to="/about" className="linkss">
              <li>About</li>
            </Link>
            <Link to="/contactus" className="linkss">
              <li>Contact Us</li>
            </Link>
          </ul>
          <hr />
          <p className="">© 2023 Ayo Jedda Vic </p>
        </div>
      </div>
    </div>
  );
}
