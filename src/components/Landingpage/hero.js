import hero from "./../../img/heroimg.webp";
import { Link } from "react-router-dom";

export default function Hero() {
  return (
    <div className="Hero_container relative d-block  d-md-flex pt-5 pt-md-0 pt-lg-5">
      <div className="hero_context container d-md-flex  justify-content-between mt-md-5 relative">
        <div className="hero_text py-5">
          <h1 className="hero_bg_text d-md-block my-4">
            MEET YOUR WOOFMATE TODAY!
          </h1>
          {/* <h2 className="hero__text">
            Our image compression website makes it easy to reduce the size of
            your images without sacrificing quality. Sign up for a free trial
            and see for yourself how much you can save in bandwidth and load
            times.
          </h2> */}
          {/* <h1 className="fs-1">
          Compress Your Images, Fast!
          </h1> */}
          <Link
            to="/compress"
            className="btn button-primary bg-black text-white rounded-pill px-4 py-2  mt-2"
            id="btnn"
          >
            SIGN UP
          </Link>
          <Link
            to="/compress"
            className="btn button-primary bg-black text-white rounded-pill px-4 py-2  mt-2"
            id="btnn"
          >
            LEARN MORE
          </Link>
        </div>
        <div className="hero_img_div m-auto">
          <img src={hero} alt="" className="hero_img" />
        </div>
      </div>
    </div>
  );
}
