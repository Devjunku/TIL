import React, {useState} from 'react'
import InputField from './movieFormComponents/InputField'


const MovieForm = ({ addMovie }) => {
  const [movieTitle, setMovieTitle] = useState('')
  const [movieYear, setMovieYear] = useState('')
  const [titleError, setTitleError] = useState('')
  const [yearError, setYearError] = useState('')

  /**
   * ... -> 구조분해 할당 extend와 비슷함
   */
  const resetForm = () => {
    if (!movieTitle && movieYear) {
      setMovieYear(movieYear)  
    } else if (movieTitle && !movieYear) {
      setMovieTitle(movieTitle)  
    } else {
      setMovieTitle("")
      setMovieYear("")
    }
  }

  const validateForm = () => {
    let validated = true
    if (!movieTitle) {
      setTitleError("영화제목을 넣어주세요")
      validated = false
    } else {
      setTitleError("")
    }

    if (!movieYear) {
      setYearError("개봉년도를 넣어주세요")
      validated = false
    } else {
      setYearError("")
    }

    return validated

  }


  const onSubmit = (event) => {
    event.preventDefault();
    if (validateForm()) {
      console.log(movieTitle, movieYear)
      addMovie({
        id: Date.now(),
        title: movieTitle,
        year: movieYear
      })
    }
    resetForm()
  }

  return (
    <form onSubmit={onSubmit}>
      <InputField
        type="text"
        value={movieTitle}
        placeholder="영화제목"
        onChange={e => setMovieTitle(e.target.value)}
        errorMessage={titleError}
        />
      <InputField
        type="number"
        value={movieYear}
        placeholder="개봉년도"
        onChange={e => setMovieYear(e.target.value)}
        errorMessage={yearError}
        />
      {/* <input
        type="text"
        value={movieTitle}
        placeholder="영화제목"
        onChange={e => setMovieTitle(e.target.value)}
        />
        <br />
        <div style={{color: 'red'}}>{titleError}</div> */}
      {/* <input
        type="number"
        value={movieYear}
        placeholder="개봉년도"
        onChange={e => setMovieYear(e.target.value)}
        />
        <div style={{color: 'red'}}>{yearError}</div> */}
        <button type="submit">영화 추가</button>
    </form>
  );
}

export default MovieForm