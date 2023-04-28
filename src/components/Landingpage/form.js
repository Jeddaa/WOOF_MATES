import React from "react";
import Darkdog from "./../../img/darkdog.jpg";

export default function Form() {

  return (
    <div className="container formcontainer">
        
      <img src={Darkdog} alt="" className="darkdog" />
      <div className="form">
        <h2 className="">FIND A DOG!</h2>
        
        <div className="inputdiv">
          <div>
            <label for="location">LOCATION</label>
            <br />
            
            <input type="text" name="location" />
          </div>

          <div>
            <label for="breed">BREED</label>
            <br />
            <input type="text" name="breed" />
          </div>

          <div className="pb-3">
            <label for="gender">GENDER </label>
            <br />
            <input type="text" name="gender" />
          </div>
        </div>
      </div>
    </div>
  );
}
