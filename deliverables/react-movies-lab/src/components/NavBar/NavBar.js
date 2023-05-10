import {Link} from "react-router-dom";


export default function NavBar({user}){
  return (
    <nav>
      <label>Hello, {user}</label>
      <Link to='/'>Movies</Link>
      &nbsp; | &nbsp;
      <Link to='/actors'>Actors</Link>
    </nav>
  )
}