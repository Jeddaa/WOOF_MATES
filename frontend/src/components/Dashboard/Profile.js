import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ProfileHeader from './ProfileHeader';
import UserDetails from './UserDetails';
import DogDetails from './DogDetails';

const Profile = () => {
  const [user, setUser] = useState(null);
  const [dogs, setDogs] = useState([]);
  const [matches, setMatches] = useState({});
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const accessToken = localStorage.getItem('access_token');

  useEffect(() => {
    const fetchUserDetails = async () => {
      try {
        const response = await axios.get('https://woof-mates.onrender.com/auth/user_with_dogs_profile', {
          headers: {
            Authorization: `${accessToken}`,
          },
        });
        setUser(response.data);
        setDogs(response.data.dogProfiles);
        setIsAuthenticated(true);

        // Fetch the matches for each dog
        const matchesData = {};
        for (const dog of response.data.dogProfiles) {
          const matchesResponse = await axios.get(`https://woof-mates.onrender.com/profile/current_user/match_all_dogs/${dog.id}`, {
            headers: {
              Authorization: `${accessToken}`,
            },
          });
          matchesData[dog.id] = matchesResponse.data.matches;
        }
        setMatches(matchesData);
      } catch (error) {
        console.error(error);
        setIsAuthenticated(false);
      }
    };

    fetchUserDetails();
  }, [accessToken]);

  return (
    <div>
      {!isAuthenticated ? (
        <p>You are not authenticated. Please log in to access this page.</p>
      ) : (
        <>
          <ProfileHeader />
          {user && <UserDetails user={user} />}
          {dogs.length > 0 && (
            <DogDetails dogs={dogs} matches={matches} />
           
          )}
        </>
      )}
    </div>
  );
};

export default Profile;