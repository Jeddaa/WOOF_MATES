import React, { useState } from 'react';
import './DogDetails.css'; // import the styling for this component

const DogDetails = ({ dogs, matches }) => {
  const [showMatches, setShowMatches] = useState(false);
  const [selectedDogId, setSelectedDogId] = useState(null);

  const handleToggleMatches = (dogId) => {
    setShowMatches(!showMatches);
    setSelectedDogId(dogId);
  };

  return (
    <div className="profile-info">
      <h2>Dog Details</h2>
      {dogs.map((dog) => (
        <div key={dog.id}>
          <h3>{dog.name}</h3>
          <p>Age: {dog.age}</p>
          <p>Breed: {dog.breed}</p>
          <p>Description: {dog.description}</p>
          <p>City: {dog.city}</p>
          <p>State: {dog.state}</p>
          <p>Country: {dog.country}</p>
          <p>Relationship Preferences: {dog.relationship_preferences}</p>
          <div className="profile-photos">
            <h2>Profile Photos</h2>
            <div className="photo-list">
              <div className="photo-item">
                <img src={dog.dog_image_1} alt={dog.name} className="photo-img"  />
              </div>
              <div className="photo-item">
                <img src={dog.dog_image_2} alt={dog.name} className="photo-img" />
              </div>
              <div className="photo-item">
                <img src={dog.dog_image_3} alt={dog.name} className="photo-img" />
              </div>
            </div>
          </div>
          <div className="matches">
            <button onClick={() => handleToggleMatches(dog.id)}>Show Matches</button>
            {showMatches && selectedDogId === dog.id && matches[selectedDogId] && matches[selectedDogId].length > 0 ? (
                <div className="profile-photos">
                <h2>Matches</h2>
                <div className="photo-list">
                    <ul>
                    {matches[selectedDogId].map((match) => (
                        <li key={match.id} className="photo-item">
                            <img src={match.profile.dog_image_3} alt={dog.name} className="photo-img" />  
                        <div className='matches-info'>
                            <h6>{match.profile.name}</h6>
                            <p>Age, {match.profile.age}</p>
                            <p>{match.profile.breed}</p>
                            <p>{match.profile.city}</p>
                        </div>
                        </li>
                    ))}
                    </ul>
                </div>
                </div>
            ) : (
                showMatches && <p>No matches yet.</p>
            )}
</div>
        </div>
      ))}
    </div>
  );
};

export default DogDetails;