import React, { useState } from 'react'
import Movie from './components/Movie'
import MovieForm from './components/MovieForm'
/**
 * useState => 바인딩 바인딩 시킬 데이터와 반영할 setData를 항상 만들어야 함
 * useEffect => rendering 될 때 마다 실행하고 싶은 로직을 쓸 때
 */

function App() {
  const [movies, setMovies] = useState([

  ])

  const removeMovie = (id) => {
    console.log(id);
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
    <div className="App">
      <h1>Movie List</h1>
      <MovieForm 
        addMovie={addMovie}
        />
      {renderMovies}
    </div>
  );
}

export default App;
