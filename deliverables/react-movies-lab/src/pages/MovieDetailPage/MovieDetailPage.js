import React from 'react'
import { useParams } from 'react-router-dom'




function MovieDetailPage(props) {
  const {movieName} = useParams();
  console.log(movieName);
  console.log(props.movies.length);
  //Use the javascript find function:
  //TODO: Create a way to move the material to the page
  const movie = props.movies.find(movie => movies.name === movieName);
  return (
    <div>
      <h1>Movie Detail Page</h1>
      <h2>{movie.name}</h2>
      <p>Director: {movie.director}</p>
      <p>Release year: {movie.releaseYear}</p>
        
    </div>
  )
}

export default MovieDetailPage