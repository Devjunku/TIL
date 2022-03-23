import React, { useEffect } from 'react'

/**
 * useState => 바인딩 바인딩 시킬 데이터와 반영할 setData를 항상 만들어야 함
 * useEffect => rendering 될 때 마다 실행하고 싶은 로직을 쓸 때
 */

function App() {
  
  useEffect(() => {
    /**
     * 컴포넌트 함수가 먼저 실행된 이후에 실행하게 됨
     */
    console.log("effect")
  })
  console.log("rendering")
  return (
    <div className="App">
      <h1>제발</h1>
    </div>
  );
}

export default App;
