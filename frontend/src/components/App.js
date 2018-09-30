import React from 'react'
import AppHeader from './AppHeader'
import Main from './Main'
import AppFooter from './AppFooter'
import './App.css'

const App = () => (
   <div className="App Site">
      <div className="Site-content">
         <div className="App-header">
            <AppHeader />
         </div>
         <div className="App-main">
            <Main />
         </div>
      </div>
      <div className="App-footer">
         <AppFooter />
      </div>
   </div>
)

export default App
