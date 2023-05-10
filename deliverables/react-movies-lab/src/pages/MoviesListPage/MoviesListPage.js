import React from 'react'
import MovieCard from '../../components/MovieCard/MovieCard'
import { movies } from '../../components/data';

function MoviesListPage(props) {
  return (
    <div className='container'>
      {
        props.movies.map(movie => {
          return <MovieCard key={movie.title} movie={movie}/>
        })
      }
      MoviesListPage
      </div>
  )
}

export default MoviesListPage