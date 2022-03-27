import React, {useState} from 'react'
import MovieForm from '../pages/MoviesComponents/MovieForm'
import Movie from '../pages/MoviesComponents/Movie'
const Movies = () => {
  const [movies, setMovies] = useState([])
  const removeMovie = (id) => {
    setMovies(
      movies.filter(movie => {
        return movie.id !== id 
      }))
  }
  const renderMovies = movies.length ? movies.map(movie => {
    return (
      <Movie 
      movie={movie}
      removeMovie={removeMovie}
      key={movie.id}/>
    )
  }) : "추가된 영화가 없습니다."

  const addMovie = (movie) => {
    setMovies([
      ...movies,
      movie
    ])
  }

  return (
    <>
      <h1>Movie List</h1>
      <MovieForm addMovie={addMovie}/>
      {renderMovies}
    </>
  );
};

export default Movies