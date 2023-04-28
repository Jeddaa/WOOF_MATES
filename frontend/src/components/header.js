import React from "react";

export default function Header() {
  return (
    <div className="">
      <div className="container text-bg-warning p-3 mt-3 d-flex align-items-center justify-content-between">
        <div className="logo ">hello world</div>
        <ul className="pagelist">
          <a>
            <li>HOME</li>
          </a>
          <a>
            <li>CONTACT</li>
          </a>
          <a>
            <li>ABOUT</li>
          </a>
        </ul>
      </div>
    </div>
  );
}
