import React from 'react'
import { Switch, Route } from 'react-router-dom'
import Home from './Home'
import About from './About'
import Nonprofits from './Nonprofits'
import ModelPage from './ModelPage'

// The Main component renders one of the provided
// Routes (provided that one matches).
const Main = () => (
  <main>
    <Switch>
      <Route exact path='/' component={Home}/>
      <Route exact path='/about' component={About}/>
      <Route exact path='/:title' component={ModelPage}/>
    </Switch>
  </main>
)

export default Main
