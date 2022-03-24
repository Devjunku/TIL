import React from 'react'
import Counter from './components/count'
/**
 * useState => 바인딩 바인딩 시킬 데이터와 반영할 setData를 항상 만들어야 함
 * useEffect => rendering 될 때 마다 실행하고 싶은 로직을 쓸 때
 */

function App() {

  return (
    <div className="App">
      <h1>제발</h1>
      <Counter/>
      <Counter/>
      <Counter/>
    </div>
  );
}

export default App;
