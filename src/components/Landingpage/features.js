import React from "react";
import Outlinepaw from "./../../img/outlinepaw.svg";
import Fairdog from "./../../img/fairdog.jpg";

function Features() {
  return (
    <div className="container mb-5">
      <h2 className="fs-1 mt-5 fw-bold">TESTIMONIES</h2>
      <hr/>
      <div className="card_container">

        <div className="grouping">
          <div className="card p-5 ">
            <img src={Fairdog} alt="" className="fairdog" />
            <img src={Outlinepaw} alt="" className="outlinepaw" />
          </div>

          <p>
            "I love using Woof Mates to connect my furry friend with other pups
            in the area. It's easy to use and has helped my dog make some great
            new friends!"
          </p>
        </div>

        <div className="grouping">
          <div className="card p-5 ">
            <img src={Fairdog} alt="" className="fairdog" />
            <img src={Outlinepaw} alt="" className="outlinepaw" />
          </div>

          <p>
            "I love using Woof Mates to connect my furry friend with other pups
            in the area. It's easy to use and has helped my dog make some great
            new friends!"
          </p>
        </div>

        <div className="grouping">
          <div className="card p-5 ">
            <img src={Fairdog} alt="" className="fairdog" />
            <img src={Outlinepaw} alt="" className="outlinepaw" />
          </div>

          <p>
            "I love using Woof Mates to connect my furry friend with other pups
            in the area. It's easy to use and has helped my dog make some great
            new friends!"
          </p>
        </div>
        
      </div>
    </div>
  );
}

export default Features;
