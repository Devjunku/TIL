import React, { useState } from 'react'
import Movie from './components/Movie'
import MovieForm from './components/MovieForm'
import Navbar from './components/Navbar'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Routes,
} from 'react-router-dom'

/**
 * useState => 바인딩 바인딩 시킬 데이터와 반영할 setData를 항상 만들어야 함
 * useEffect => rendering 될 때 마다 실행하고 싶은 로직을 쓸 때
 */

function App() {
  const [movies, setMovies] = useState([ ])

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
    <Router>
      <div className="App">
        <Navbar/>
        <Switch>
          <Route path="/movies">
            <h1>Movie List</h1>
            {renderMovies}
            <MovieForm 
              addMovie={addMovie}
              />
          </Route>
          <Route path="/users" exact>
            <h1>Users</h1>
          </Route>
          <Route path="/">
            <h1>Home </h1>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
