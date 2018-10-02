import React from 'react'
import { Switch, Route } from 'react-router-dom'
import Home from './Home'
import About from './About'
import ModelPage from './ModelPage'
import LocationPage from './LocationPage'
import CategoryPage from './CategoryPage'
import NonprofitPage from './NonprofitPage'

// The Main component renders one of the provided
// Routes (provided that one matches).
const Main = () => (
  <main>
    <Switch>
      <Route exact path='/' component={Home}/>
      <Route exact path='/about' component={About}/>
      <Route exact path='/:title' component={ModelPage}/>
      <Route exact path='/location/:id' component={LocationPage}/>
      <Route exact path='/category/:id' component={CategoryPage}/>
      <Route exact path='/nonprofit/:id' component={NonprofitPage}/>
    </Switch>
  </main>
)

export default Main
