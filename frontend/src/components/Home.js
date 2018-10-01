import React from 'react'
import { Jumbotron, Button } from 'reactstrap'

const Home = () => (
   <div className="container">
      <Jumbotron>
         <h1>Welcome to NPOLink!</h1>
         <p>
            Learn more about nonprofits in your area and how you can contribute.
         </p>
         <Button bsStyle="primary">Learn more</Button>
      </Jumbotron>
   </div>
)

export default Home
