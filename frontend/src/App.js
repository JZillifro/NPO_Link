import React, { Component } from 'react';
import logo from './logo.svg';
import {BrowserRouter, Route, Switch, Redirect} from 'react-router-dom';
import './App.css';
import Home from './components/Home';

class App extends Component {
  render() {
    return (
      <div className="App">
        <BrowserRouter>
        <div>
          <Switch>
            <Route exact path="/" component={Home}/>
          <Redirect from='*' to='/404' status={404}/>
          </Switch>
        </div>
      </BrowserRouter>
      </div>
    );
  }
}

export default App;
