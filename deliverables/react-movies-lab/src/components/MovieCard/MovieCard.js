import React from 'react'
import { useState, useEffect } from 'react'
import {Link} from 'react-router-dom'


function MovieCard(props) {
  console.log(props);
  return (
    <div>
      {props.movie.title}

    </div>
  )

  
}

export default MovieCard

