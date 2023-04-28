import { useContext } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faCaretDown, faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import { AuthContext } from '../Account/AuthProvider';

function ProfileHeader() {
  const { logout } = useContext(AuthContext);

  const handleMenuClick = () => {
    const menu = document.querySelector('.profile-header-menu');
    menu.classList.toggle('show');
  };

  const handleLogoutClick = () => {
    logout();
  };

  return (
    <div className="profile-header">
      <div className="profile-header-left">
        <div className="back-arrow">
        <a href="/homefeed">
            <FontAwesomeIcon icon={faArrowLeft} />
        </a>
        </div>
        <div className="profile-heading">
          <h1>Woof Mates Profile</h1>
        </div>
      </div>
      <div className="profile-header-right">
        <div className="profile-header-menu-container">
          <button onClick={handleMenuClick}>
            <FontAwesomeIcon icon={faUser} />
            <FontAwesomeIcon icon={faCaretDown} />
          </button>
          <ul className="profile-header-menu">
            <li><a href="#">My Profile</a></li>
            <li><a href="">Settings</a></li>
            <li><a href="/" onClick={handleLogoutClick}>Logout</a></li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default ProfileHeader;