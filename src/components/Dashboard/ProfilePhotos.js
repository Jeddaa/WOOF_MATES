import React, { useState, useEffect } from 'react';

const ProfilePhotos = () => {
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    fetch('https://dog.ceo/api/breeds/image/random/3')
      .then((response) => response.json())
      .then((data) => setPhotos(data.message))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div className="profile-photos">
      <h2>Profile Photos</h2>
      <div className="photo-list">
        {photos.map((photo, index) => (
          <div key={index} className="photo-item">
            <img src={photo} alt={`Dog photo ${index}`} className="photo-img" />
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProfilePhotos;
