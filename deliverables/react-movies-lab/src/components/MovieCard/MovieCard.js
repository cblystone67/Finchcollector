import './MovieCard.css';
import React from 'react'

import {Link} from 'react-router-dom'


function MovieCard(props) {
  console.log(props);
  return (
    <div className='movie-card'>
      {props.movie.title}
    <img alt="Movie Poster" src={props.movie.posterPath}/>
      {props.movie.releaseDate}
      <Link to={`/movies/${props.movie.title}`}>Movie Details</Link>
    </div>
  )

  
}

export default MovieCard

