import React from 'react'
import { Switch, Route } from 'react-router-dom'
import Home from './Home'
import About from './About'

// The Main component renders one of the provided
// Routes (provided that one matches).
const Main = () => (
  <main>
    <Switch>
      <Route exact path='/' component={Home}/>
      <Route exact path='/about' component={About}/>
    </Switch>
  </main>
)

export default Main
