import Aboutimg from "./../img/about.webp";
import Navbar from "./Landingpage/navbar";
import { Link } from "react-router-dom";
import Footer from "./Landingpage/footer";
import Jedda from "./../img/jedda.webp";
import Victor from "./../img/vic.webp";
import Ay from "./../img/ay.webp";
import Farida from "./../img/farida.jpg";

function About() {
  return (
    <div className="aboutt">
      <Navbar />
      <div className="about_div">
        <div className="div">
          <h1>ABOUT</h1>
        </div>
        <div
          style={{ backgroundImage: `url(${Aboutimg})` }}
          className="about_header"
        >
          <div id="overlay"></div>
        </div>
      </div>
      <div className="container t py-5 text">
        <p>
          We are a dedicated team of 4 software engineers who are passionate
          about creating tools that help our everyday life.
          {/* <hr /> */}
          <br />
          <br />
          Welcome to Woof mates, the ultimate platform for dog owners and
          enthusiasts to connect and find the perfect match for their furry
          friends. Our mission is to help dogs and their owners form lasting
          relationships that bring joy, companionship, and adventure into their
          lives.
          <br />
          <br />
          At woof mates, we understand that every dog has unique needs and
          personalities. That's why we offer a range of options, from playmates
          to breeding partners, service dog partners to training partners, and
          everything in between. Our advanced matching algorithm ensures that
          every match is tailored to your preferences, so you can find the
          perfect fit for your furry friend.
          <br />
          <br />
          We believe that dogs bring so much happiness and love into our lives,
          and we're passionate about helping more people experience that joy.
          Whether you're a dog owner looking for a new friend for your pup, or a
          dog lover looking to connect with other dog enthusiasts, Woof mates is
          the perfect place to find your match.
          <br />
          <br />
          Join our community today and experience the joy of finding the perfect
          match for your furry friend!
          <br />
          <br />
          At Woof mates, we're dedicated to creating an exceptional experience
          for dog owners and enthusiasts. We're proud of the work we've done to
          develop our platform and are constantly striving to improve it. Our
          mission is to help you find the perfect playmate, training partner,
          breeding partner, service dog partner, or companion for your furry
          friend. Thank you for choosing Woof mates - we're thrilled to be a
          part of your journey with your beloved pet.
          {/* <hr /> */}
          <br />
          <br />
          <br />
          Please{" "}
          <Link to="/contactus" className="about_link">
            {" "}
            let us know
          </Link>{" "}
          if you have any question or need any further assistance.
        </p>
      </div>
      <div className="">
        <hr className="mb-5 " />
        <h1 className="text-center fw-bold fs-1 mt-5 mb-4">MEET THE TEAM</h1>

        <div className="meet_div">
          <div>
            <div className="team_card rounded">
              <img
                src={Jedda}
                className="rounded-pill img-thumbnail meet_img"
                alt=""
              />
              <h4>Fatihah Oduwole</h4>
              <div className="socials">
                <a href="mailto:fathiato@gmail.com" target="_blank">
                  <ion-icon name="mail-outline" className="icon"></ion-icon>
                </a>
                <a
                  href="https://www.linkedin.com/in/fatihahoduwole/"
                  target="_blank"
                >
                  <ion-icon name="logo-linkedin" className="icon"></ion-icon>
                </a>
                <a href="" target="_blank">
                  <ion-icon name="logo-twitter" className="icon"></ion-icon>
                </a>
                <a href="https://github.com/Jeddaa" target="_blank">
                  <ion-icon name="logo-github" className="icon"></ion-icon>
                </a>
              </div>
            </div>
          </div>

          <div>
            <div className="team_card rounded">
              <img
                src={Victor}
                className="rounded-pill img-thumbnail meet_img"
                alt=""
              />
              <h4>Victor Nwosu</h4>
              <div className="socials">
                <a href="mailto:nwosuvictor54@gmail.com" target="_blank">
                  <ion-icon name="mail-outline" className="icon"></ion-icon>
                </a>
                <a
                  href="https://www.linkedin.com/in/nwosu-victor/"
                  target="_blank"
                >
                  <ion-icon name="logo-linkedin" className="icon"></ion-icon>
                </a>
                <a href="https://twitter.com/__chi__mo__" target="_blank">
                  <ion-icon name="logo-twitter" className="icon"></ion-icon>
                </a>
                <a href="https://github.com/vicNW" target="_blank">
                  <ion-icon name="logo-github" className="icon"></ion-icon>
                </a>
              </div>
            </div>
          </div>

          <div>
            <div className="team_card rounded">
              <img
                src={Farida}
                className="rounded-pill img-thumbnail meet_img"
                alt=""
              />
              <h4>Fatihah Oduwole</h4>
              <div className="socials">
                <a href="mailto:fathiato@gmail.com" target="_blank">
                  <ion-icon name="mail-outline" className="icon"></ion-icon>
                </a>
                <a
                  href="https://www.linkedin.com/in/fatihahoduwole/"
                  target="_blank"
                >
                  <ion-icon name="logo-linkedin" className="icon"></ion-icon>
                </a>
                <a href="" target="_blank">
                  <ion-icon name="logo-twitter" className="icon"></ion-icon>
                </a>
                <a href="https://github.com/Jeddaa" target="_blank">
                  <ion-icon name="logo-github" className="icon"></ion-icon>
                </a>
              </div>
            </div>
          </div>

          <div>
            <div className="team_card rounded">
              <img
                src={Ay}
                className="rounded-pill img-thumbnail meet_img"
                alt=""
              />
              <h4>Ayomide Soniyi</h4>
              <div className="socials">
                <a href="mailto:ayomidesoniyi@gmail.com" target="_blank">
                  <ion-icon name="mail-outline" className="icon"></ion-icon>
                </a>
                <a
                  href="https://www.linkedin.com/in/ayomide-soniyi-3151461a5"
                  target="_blank"
                >
                  <ion-icon name="logo-linkedin" className="icon"></ion-icon>
                </a>
                <a
                  href="https://twitter.com/SoniyiAyomide_?t=tteA9SCa6-iCUr6XVztPCg&s=09"
                  target="_blank"
                >
                  <ion-icon name="logo-twitter" className="icon"></ion-icon>
                </a>
                <a href="https://github.com/UnfazedAy" target="_blank">
                  <ion-icon name="logo-github" className="icon"></ion-icon>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default About;
