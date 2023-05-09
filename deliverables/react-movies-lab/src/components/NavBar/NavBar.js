import {Link} from "react-router-dom";


export default function NavBar(){
  return (
    <nav>
      <Link to='/MoviesListPage'></Link>
      &nbsp; | &nbsp;
      <Link to='/ActorListPage'></Link>
    </nav>
  )
}