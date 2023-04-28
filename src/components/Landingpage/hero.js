import hero from "./../../img/heroimg.png";
import { Link } from "react-router-dom";

export default function Hero() {
  return (
    <div className="Hero_container relative d-block  d-md-flex pt-5 pt-md-0 pt-lg-5">
      <div className="hero_context container d-md-flex  justify-content-between mt-md-5 relative">
        <div className="hero_text py-5">
          <h1 className="hero_bg_text d-md-block my-4">
            MEET YOUR WOOFMATE TODAY!
          </h1>
          <h2 className="hero__text">
            Find your perfect dog match with our site, designed for those
            seeking Playmates, Training Partners, Breeding Partners, Service Dog
            Partners, and Companionship.
          </h2>

          <Link
            to="/register"
            className="btn button-primary bg-black text-white rounded-pill px-4 py-2  mt-2"
            id="btnn"
          >
            SIGN UP
          </Link>
          
        </div>
        <div className="hero_img_div m-auto">
          <img src={hero} alt="" className="hero_img" />
        </div>
      </div>
    </div>
  );
}
