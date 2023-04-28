import Contactimg from "./../img/contactus.webp";
import Navbar from "./Landingpage/navbar";
import Footer from "./Landingpage/footer";

function contact() {
  return (
    <div>
      <Navbar />
      <div className="about_div">
        <div className="div">
          <h1>CONTACT US</h1>
        </div>

        <div
          style={{ backgroundImage: `url(${Contactimg})` }}
          className="about_header"
        >
          <div id="overlay"></div>
        </div>
      </div>

      <form className="my-5 container" method="POST">
        <input
          type="name"
          placeholder="Name"
          className="signin-field p-3 my-3"
        />
        <input
          type="email"
          placeholder="Email"
          className="signin-field p-3 my-3"
        />

        <textarea
          className="signin-field ta p-3 my-3"
          placeholder="Message"
          rows="5"
        ></textarea>
        <button type="submit" className="buttonn p-3 mb-5">
          Submit
        </button>
      </form>

      <Footer />
    </div>
  );
}

export default contact;
