import "./chat.css";
import React from "react";
import Victor from "./../img/vic.webp";

export default function Chat() {
  return (
    <div>
      <div className="sidenav"></div>

      <div className="chattingArea">
        <div className="headerr">
          <div className="d-flex align-items-center">
            <img
              src={Victor}
              className="rounded-pill img-thumbnail chat_pfp"
              alt=""
            />
            <div className="header_details">
              <h3 className="m-0">Nwosu Victor</h3>
              <p className="m-0 h6">
                <i>online</i>
              </p>
            </div>
          </div>
          <div className="me-2 icons_div d-flex align-items-center">
            <ion-icon name="videocam-outline"></ion-icon>
            <ion-icon name="call-outline"></ion-icon>
            <div className="last_icon d-flex align-items-center p-3">
              <ion-icon name="search-outline"></ion-icon>
            </div>
          </div>
        </div>

        <div className="chat_footer d-flex align-items-center">
        <ion-icon name="happy-outline" ></ion-icon>
          <textarea type="text" className="typing_area" />
          <ion-icon name="send-outline"></ion-icon>
        </div>
      </div>
    </div>
  );
}