import ProfileHeader from './ProfileHeader'
import ProfileInfo from './ProfileInfo'
import ProfilePhotos from './ProfilePhotos'
import ProfileMatches from './ProfileMatches'


const Profile = () => {
  return (
    <div className='profile'>
    <ProfileHeader />
    <ProfileInfo />
    <ProfilePhotos />
    <ProfileMatches />
    </div>
  )
}

export default Profile