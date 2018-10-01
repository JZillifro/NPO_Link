import React from 'react'
import { Switch, Route } from 'react-router-dom'
import Home from './Home'
import About from './About'
import ModelPage from './ModelPage'
import LocationPage from './LocationPage'

// The Main component renders one of the provided
// Routes (provided that one matches).
const Main = () => (
  <main>
    <Switch>
      <Route exact path='/' component={Home}/>
      <Route exact path='/about' component={About}/>
      <Route exact path='/nonprofits' component={ModelPage}/>
      <Route exact path='/locations' component={ModelPage}/>
      <Route exact path='/categories' component={ModelPage}/>
      <Route exact path='/locations/:city' component={LocationPage}/>
    </Switch>
  </main>
)

export default Main
