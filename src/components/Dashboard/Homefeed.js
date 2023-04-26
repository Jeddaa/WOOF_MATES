import React, { useState, useEffect } from 'react';
import axios from 'axios';
import DogCard from './DogCard';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faEnvelope } from '@fortawesome/free-solid-svg-icons';
import Conversation from './Conversation';

function HomeFeed() {
  const [dogs, setDogs] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [conversationVisible, setConversationVisible] = useState(false);

  useEffect(() => {
    setIsLoading(true);
    setError(null);
    axios.get('https://dog.ceo/api/breeds/image/random/100')
      .then(response => {
        const newDogs = response.data.message.map((imageUrl, index) => ({
          id: index,
          name: `Dog ${index + 1}`,
          breed: 'Unknown',
          age: Math.floor(Math.random() * 10) + 1,
          location: 'Unknown',
          imageUrl,
        }));
        setDogs(newDogs);
        setIsLoading(false);
      })
      .catch(error => {
        console.log(error);
        setError(error);
        setIsLoading(false);
      });
  }, []);

  function handleSwipeLeft() {
    const [firstDog, ...remainingDogs] = dogs;
    setDogs(remainingDogs.concat(firstDog));
  }

  function handleSwipeRight() {
    const [firstDog, ...remainingDogs] = dogs;
    setDogs(remainingDogs);
  }

  function handleToggleConversation() {
    setConversationVisible(!conversationVisible);
  }

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (dogs.length === 0) {
    return <div>No more dogs to swipe on!</div>;
  }

  return (
    <div className="home-feed">
      <div className="header">
      <a href="/profile">
        <FontAwesomeIcon icon={faHome} className='header-icon' />
      </a>
        <h1>Home Feed</h1>
        <FontAwesomeIcon icon={faEnvelope} className='header-icon' onClick={handleToggleConversation} />
      </div>
      {conversationVisible && <Conversation onClose={handleToggleConversation}/>}
      <div className='dogcard-container'>
        <DogCard dog={dogs[0]} onSwipeLeft={handleSwipeLeft} onSwipeRight={handleSwipeRight} />
      </div>
    </div>
  );
}

export default HomeFeed;