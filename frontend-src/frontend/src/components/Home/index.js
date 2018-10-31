import React from 'react';
import Image from "../../hands.jpg"

export default class Home extends React.Component {
  render() {
    return (
      <div id="header" style={{backgroundImage: `url(${Image})`}}>
        <div className="inner">
          <header>
            <h1>NPOLink</h1>
            <br />
            <p>Learn more about nonprofits in your area and how you can contribute.</p>
          </header>
        </div>
      </div>
    )
  }
}
