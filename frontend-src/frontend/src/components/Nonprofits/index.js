import React, { Component } from 'react'
import { PageHeader } from 'react-bootstrap'

class Nonprofits extends Component {
  constructor(props) {
    super(props);
    this.state = {
      contributors: []
    };
  }

  componentDidMount() {

  };

  render() {
    return (
        <div className="container">
          <PageHeader>
           Example page header <small>Subtext for header</small>
          </PageHeader>
       </div>
    );
  }
}

export default Nonprofits;
