import React from 'react';
import './css/UserDetails.css';

const UserDetails = ({ user }) => {
  return (
    <div className="profile">
      <div className="photo-item photo">
        <img src={user.profile_picture} style={{ width: '200px', height: '200px' }} alt={user.firstName} />
      </div>
      <div className="info">
        <h2>User Details</h2>
        <p>Name: {user.firstName} {user.lastName}</p>
        <p>Email: {user.email}</p>
      </div>
    </div>
  );
};

export default UserDetails;