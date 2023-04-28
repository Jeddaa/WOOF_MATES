import React from 'react'

const ProfileInfo = ({ name, age, breed, location }) => {
  return (
    <div className="profile-info">
      <h2>Profile Info</h2>
      <p>Name: {name}</p>
      <p>Age: {age}</p>
      <p>Breed: {breed}</p>
      <p>Location: {location}</p>
    </div>
  )
}

export default ProfileInfo