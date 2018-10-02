import React from 'react';
import {Jumbotron, Button, PageHeader} from 'react-bootstrap';

export default class Home extends React.Component {
  render() {
    return (
      <div className="container" >
        <PageHeader style={{backgroundColor: "#b4eeb4"}}>
          <div style={{marginLeft: "20px", textAlign: "center"}}>
            <br/>
            <h1>Welcome to NPOLink!</h1>
            <small>
               Learn more about nonprofits in your area and how you can contribute.
            </small>
          </div>
        </PageHeader>
        <img src="https://openclipart.org/download/276483/1490609861.svg" style={{width:"70%", display:"block", marginLeft:"auto", marginRight:"auto"}}/>
      </div>
    )
  }
}
