import React, { useState } from 'react'
import './App.css';
import { createStore } from 'redux'
import {Provider, useSelector, useDispatch} from 'react-redux'
/**
 * Provider
 * useSelector
 * useDispatch
 * 
 */

function reducer(currentState, action) {
  if (currentState === undefined) {
    return {
      number:1
    }
  }
  const newState = {...currentState}
  if (action.type == "PLUS") {
    newState.number ++
  }
  return newState
}


const store = createStore(reducer);
function App() {

  return (
    <div id="container">
      <h1>Root:</h1>
      <div id="grid">
        <Provider store={store}>
          <Left1/>
          <Right1/>
        </Provider>
      </div>
    </div>
  );
}

function Left1(props) {
  const number = useSelector((state) => state.number)
  return (
    <div>
      <h1>Left1 : {number} </h1>
      <Left2 
       
      />
    </div>
  )
}

function Left2(props) {
  const number = useSelector((state) => state.number)
  return (
    <div>
      <h1>Left2 : {number} </h1>
      <Left3
        
      />
    </div>
  )
}

function Left3(props) {
  
  const number = useSelector((state) => state.number)

  return (
    <div>
      <h1>Left3 : {number}</h1>
    </div>
  )
}

function Right1(props) {
  return (
    <div>
      <h1>Right1</h1>
      <Right2
        
      />
    </div>
  )
}

function Right2(props) {
  return (
    <div>
      <h1>Right2</h1>
      <Right3
        
      />
    </div>
  )
}

function Right3(props) {
  const dispatch = useDispatch()
  return (
    <div>
      <h1>Right3</h1>
      <input
        type="button"
        value="+"
        onClick={() => {
          dispatch({
            type: 'PLUS'
          })
        }} />
    </div>
  )
}


export default App;
