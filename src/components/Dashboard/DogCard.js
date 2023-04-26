import React from 'react';

function DogCard({ dog, onSwipeLeft, onSwipeRight }) {
  return (
    <div className="dog-card" style={{ backgroundImage: `url(${dog.imageUrl})` }}>
      <div className="dog-details">
        <h2>{dog.name}</h2>
        <p>Breed: {dog.breed}</p>
        <p>Age: {dog.age} years old</p>
        <p>Location: {dog.location}</p>
      </div>
      <div className="swipe-buttons">
        <button className="swipe-left" onClick={onSwipeLeft}>❌</button>
        <button className="swipe-right" onClick={onSwipeRight}>❤️</button>
      </div>
    </div>
  );
}

export default DogCard;
