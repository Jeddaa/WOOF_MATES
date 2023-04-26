import React, { useState, useEffect } from 'react';

const ProfileMatches = () => {
  const [dogBreeds, setDogBreeds] = useState([]);
  const [dogMatches, setDogMatches] = useState([]);

  useEffect(() => {
    // Fetch list of dog breeds
    fetch('https://dog.ceo/api/breeds/list/all')
      .then(response => response.json())
      .then(data => {
        const breeds = Object.keys(data.message);
        setDogBreeds(breeds);
      })
      .catch(error => console.error(error));
  }, []);

  const handleFetchDogMatches = () => {
    // Fetch 3 random images of dogs and their breed
    const promises = [];
    for (let i = 0; i < 3; i++) {
      const breed = dogBreeds[Math.floor(Math.random() * dogBreeds.length)];
      const promise = fetch(`https://dog.ceo/api/breed/${breed}/images/random`)
        .then(response => response.json())
        .then(data => ({
          breed: breed,
          image: data.message,
        }));
      promises.push(promise);
    }
    Promise.all(promises)
      .then(matches => setDogMatches(matches))
      .catch(error => console.error(error));
  };

  return (
    <div className="profile-matches">
      <h2>Profile Matches</h2>
      <button  className="btn button-primary bg-black text-white  rounded-pill px-4 py-2  mt-2"
            id="btnn" onClick={handleFetchDogMatches}>
              Fetch Dog Matches
              </button>
      <ul className="match-list">
        {dogMatches.map(match => (
          <li key={match.breed} className="match-item">
            <img src={match.image} alt={match.breed} />
            <div className="match-details">
              <h3>{match.breed}</h3>
              <p>Breed: {match.breed}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProfileMatches;
