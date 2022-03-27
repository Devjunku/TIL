import React from 'react'
import Navbar from './AppComponents/Navbar'
import routes from './routes'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom'

/**
 * useState => 바인딩 바인딩 시킬 데이터와 반영할 setData를 항상 만들어야 함
 * useEffect => rendering 될 때 마다 실행하고 싶은 로직을 쓸 때
 */

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar/>
          <div className="container">
          <Switch>
            {routes.map(route => {
              return (
                <Route
                  key={route.path}
                  path={route.path}
                  exact>
                  <route.component/>
                </Route>
              )
            })}
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
