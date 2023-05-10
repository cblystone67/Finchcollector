import './MovieCard.css';
import React from 'react'
import { useState, useEffect } from 'react'
import {Link} from 'react-router-dom'


function MovieCard(props) {
  console.log(props);
  return (
    <div className='movie-card'>
      {props.movie.title}
    <img src={props.movie.posterPath}/>
      {props.movie.releaseDate}
    </div>
  )

  
}

export default MovieCard

