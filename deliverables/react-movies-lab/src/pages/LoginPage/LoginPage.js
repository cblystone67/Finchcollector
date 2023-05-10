import {useState} from 'react'


export default function LoginPage({setUser}){
  const [newUser, setNewUser] = useState('');
  const handleChange = (evt) => {
    setNewUser(evt.target.value);
  };

  const handleSubmit = (evt) => {
    evt.preventDefault();
    setUser(newUser);
  };

  return (
    <div className="LoginPage">
      <h1>Login Page</h1>
      <form onSubmit={handleSubmit}>
        <input 
        type='text' 
        value={newUser} 
        onChange={handleChange} 
        placeholder='Enter UserName' 
        />
        <button type='submit'>Add User</button>
      </form>
      
    </div>
  )
};